from django.db import models
from django.utils import timezone
# Create your models here.
class cartype(models.Model):
    BRANDS = [
        ('AMR','ASTON MARTIN'),
        ('BMW','BAYES MOTOR WORKS'),
        ('AMG','MERCEDES AMG'),
        ('BNZ','MERCEDES BENZ'),
        ('BGT','BUGGATI'),
        ('POR','PORSCHE'),
    ]
    name= models.CharField(max_length=50)
    image= models.ImageField(upload_to='bonk/static/')
    brand= models.CharField(max_length=50)
    power= models.CharField(max_length=50)
    sold_date= models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=3, choices=BRANDS)