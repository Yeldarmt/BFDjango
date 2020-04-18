from django.core.management.base import BaseCommand
from onlineShop.api.models import Product
from onlineShop.main.models import Category
from django.db.models import Avg, Max, Min, Sum


class Command(BaseCommand):
    help = 'Delete Products from table'

    def handle(self, *args, **kwargs):
        self.stdout.write(str(Product.objects.aggregate(Avg('price'))))
        self.stdout.write(str(Product.objects.aggregate(Max('price'))))
        self.stdout.write(str(Product.objects.aggregate(min_price=Min('price'))))
        self.stdout.write(str(Product.objects.aggregate(Sum('price'))))
