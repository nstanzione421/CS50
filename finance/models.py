from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    company = models.CharField(max_length=255)

    def serialize(self):
        return {
            "id": self.id,
            "stock": self.stock,
            "company": self.company
        }

class Trade(models.Model):
    trader = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="volume")
    transaction = models.CharField(max_length=10)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "trader": self.trader.username,
            "stock": self.stock.ticker,
            "transaction": self.transaction,
            "quantity": self.quantity,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
        }
