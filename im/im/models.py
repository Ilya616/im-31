from django.db import models
from django_seed import Seed


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


class Role(models.Model):
    name = models.CharField(max_length=20)


# class Seed(models.Model):
    
#     seeder = Seed.seeder()
#     seeder.add_entity(Role, 2, {
#     'name': 'user',
# })

