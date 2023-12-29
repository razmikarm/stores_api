from django.db import models

class Store(models.Model):
    
    address = models.TextField("address")
    capacity = models.IntegerField("capacity", default=200)
    products = models.ManyToManyField('Product', related_name='stores', default=None, blank=True)

    def __str__(self):
        return self.address


class Product(models.Model):
    
    name = models.CharField("name", max_length=30)
    size = models.IntegerField("size", default=1)
    price = models.IntegerField("price")

    def __str__(self):
        return self.name


# class ProductStore(models.Model):
