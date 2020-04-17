from rest_framework import serializers
from onlineShop.api.models import Product
from onlineShop.main.serializers import CategorySerializer
import logging

logger = logging.getLogger('main')


# class ProductShortSerializer(serializers.ModelSerializer):
#     category_id = serializers.IntegerField(write_only=True)
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'count', 'category_id')
#
#
# class ProductFullSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True)
#
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price', 'count', 'category')

class ProductShortSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'photo', 'price', 'count', 'category_id')

    def validate_count(self, value):
        if value < 0:
            logger.debug(f'Product not created, count can not be less than 0')
            logger.info(f'Product not created, count can not be less than 0')
            logger.warning(f'Product not created, count can not be less than 0')
            logger.error(f'Product not created, count can not be less than 0')
            logger.critical(f'Product not created, count can not be less than 0')
            raise serializers.ValidationError('less than null')
        return value


class ProductFullSerializer(ProductShortSerializer):
    category = CategorySerializer(read_only=True)

    class Meta(ProductShortSerializer.Meta):
        model = Product
        fields = ProductShortSerializer.Meta.fields + ('category',)
