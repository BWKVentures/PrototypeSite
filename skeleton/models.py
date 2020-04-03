from django.db import models

# Create your models here.

class UserDatabase(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

class ItemDatabase(models.Model):
    item_name = models.CharField(max_length=30)
    item_price = models.DecimalField(max_digits=100,decimal_places=2)
    date_available = models.DateField()
