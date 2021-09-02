from django.db import models
import datetime
from django.utils import timezone
from django.utils.timezone import now
# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=100)
    image = models.URLField(max_length=200,)
    timeStamps = models.DateTimeField(default=now, blank=True)
    def __str__(self):
        return self.name

class cart(models.Model):
    pizza_name = models.CharField(max_length=130)
    Number_of_pizza = models.IntegerField()
    Grand_total = models.IntegerField()
    def __str__(self):
        return self.pizza_name
