from django.db import models

from onlineShop.main.models import Category


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name