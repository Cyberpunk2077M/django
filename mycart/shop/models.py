from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50)
    price=models.IntegerField(default=1)
    desc=models.CharField(max_length=5000)
    pub_date=models.DateField()
    image = models.ImageField(upload_to='shop/images')
    
    def __str__(self):
        return f"{self.product_name} {self.category} {self.subcategory} {self.pub_date}"
