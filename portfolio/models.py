from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import Portfolio

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    buying_price = models.FloatField()
    buying_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Stock-->" + self.name + " " + "Quantity-->" + str(self.quantity) + " " +  "Quantity-->" + str(self.buying_price) + " "