from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class cartype(models.Model):
    CLASS = [
        ('ETT','Extreme Track Toys'),
        ('TT_','Track Toys'),
        ('OR_','Off Road'),
        ('EOR','Extreme Off Road'),
        ('GT_','GT'),
        ('SGT','Super GT'),
        ('DFT','Drift'),
    ]
    name= models.CharField(max_length=50)
    image= models.ImageField(upload_to='bonk/static/')
    brand= models.CharField(max_length=50)
    power= models.CharField(max_length=50)
    sold_date= models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=3, choices=CLASS)
    description = models.TextField(default='')
    nationality= models.TextField(default='unavailable')

def __str__(self):
    return self.name

class Car_Review(models.Model):
    car=models.ForeignKey(cartype, on_delete=models.CASCADE, related_name='review')
    buyer=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    experience=models.TextField(default='')
    date_added=models.DateTimeField(default=timezone.now)

def __str__(self):
    return f'{self.user.username} review for {self.cartype.name}'
