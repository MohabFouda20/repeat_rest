from django.db import models

# Create your models here.
class Product(models.Model):
   title = models.CharField(max_length=120)
   content = models.TextField(null=True, blank=True)
   price  = models.DecimalField(decimal_places=2, max_digits=20 , default=100.00)
   
   
   @property
   def sale_price(self):
       return "%.2f"%(float(self.price) * 0.8)