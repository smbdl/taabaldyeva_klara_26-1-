from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    rate = models.FloatField(default=0.0)
