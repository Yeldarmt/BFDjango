from django.db import models
from onlineShop.main.models import Category

import os
from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.jpg', '.png']


def validate_file_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'max file size is: {MAX_FILE_SIZE}')


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='author_photos',
                              validators=[validate_file_size,
                                          validate_extension],
                              null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return 'product name: {}, id: {}'.format(self.name, self.id)

    def top_three(self):
        three = Product.objects.all()[:3]
        return three
