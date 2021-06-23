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
    image = models.ImageField()
    timeStamps = models.DateTimeField(default=now, blank=True)
    def __str__(self):
        return self.name