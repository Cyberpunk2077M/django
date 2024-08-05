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
    return f"{self.brand}{self.name}"

#one to many:
class Car_Review(models.Model):
    car=models.ForeignKey(cartype, on_delete=models.CASCADE, related_name='review')
    buyer=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    experience=models.TextField(default='')
    date_added=models.DateTimeField(default=timezone.now)

def __str__(self):
    return f'{self.user.username} review for {self.cartype.name}'

#many to many
class dealership(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    carname=models.ManyToManyField(cartype, verbose_name="dealerships")

def __str__(self):
    return f"{self.name} {self.cartype.name}"

#One to One
class regno(models.Model):
    car=models.OneToOneField(cartype, verbose_name="registration", on_delete=models.CASCADE)
    reg_no=models.CharField(max_length=8)
    reg_date=models.DateField(auto_now=True)

def __str__(self):
    return f'Registration no. for {self.cartype.name}'