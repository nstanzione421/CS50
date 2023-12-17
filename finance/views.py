from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import User, Stock, Trade

# Create your views here.

def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "finance/stocks.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))


@csrf_exempt
@login_required
def trade(request):

    # Composing a new email must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Get contents of trade

    data = json.loads(request.body)
    transaction = data.get("transaction")
    ticker = data.get("ticker")
    quantity = int(data.get("quantity"))

    # Check trade information is complete
    if ticker == "":
        return JsonResponse({
            "error": "Ticker symbol required."
        }, status=400)
    
    if quantity <= 0:
        return JsonResponse({
            "error": "Number of shares (quantity) required."
        }, status=400)

    allStocks = Stock.objects.all().order_by('id')

    tickers = []
    for stock in allStocks:
        tickers.append(stock.ticker)

    if ticker not in tickers:
        return JsonResponse({
            "error": "Stock not available on this exchange."
        }, status=400)
        
    selectedStock = Stock.objects.get(ticker=ticker)

    # Create trade
    trade = Trade(
        trader=request.user,
        transaction=transaction,
        stock=selectedStock,
        quantity=quantity
    )
    trade.save()

    return JsonResponse({"message": "Trade executed successfully."}, status=201)


@login_required
def history(request):

    # Filter trades returned based on mailbox
    trades = Trade.objects.filter(
        trader=request.user
    )

    # Return trades in reverse chronologial order
    trades = trades.order_by("-timestamp").all()
    return JsonResponse([trade.serialize() for trade in trades], safe=False)


@login_required
def account(request):
    return render(request, "finance/stocks.html")


@csrf_exempt
@login_required
def transaction(request, trade_id):

    # Query for requested trade
    try:
        trade = Trade.objects.get(trader=request.user, pk=trade_id)
    except Trade.DoesNotExist:
        return JsonResponse({"error": "Trade not found."}, status=404)

    # Return trade contents
    if request.method == "GET":
        return JsonResponse(trade.serialize())
 
    # Trade must be via GET
    else:
        return JsonResponse({
            "error": "GET request required."
        }, status=400)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finance/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "finance/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "finance/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "finance/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "finance/register.html")
