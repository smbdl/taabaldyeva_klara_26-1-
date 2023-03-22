from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media/product_images')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    rate = models.FloatField(default=0.0)


class Review(models.Model):
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
