from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    old_price = models.FloatField()
    descriptrion_product = models.TextField()
    count = models.IntegerField()
    category = models.ForeignKey("CategoryProduct",  on_delete=models.CASCADE)


class CategoryProduct(models.Model):
    name = models.CharField(max_length=20)
    descriptrion_category = models.TextField()



