from django.db import models
from django.utils import timezone
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

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
