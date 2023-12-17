from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("trades", views.trade, name="trade"),
    path("trades/<int:trade_id>", views.transaction, name="transaction"),
    path("trades/history", views.history, name="history"),
    path("trades/account", views.account, name="account")
]
