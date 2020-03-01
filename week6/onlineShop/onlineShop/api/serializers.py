from rest_framework import serializers
from onlineShop.api.models import Product
from onlineShop.main.serializers import CategorySerializer


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
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'count', 'category_id')


class ProductFullSerializer(ProductShortSerializer):
    category = CategorySerializer(read_only=True)

    class Meta(ProductShortSerializer.Meta):
        model = Product
        fields = ProductShortSerializer.Meta.fields + ('category',)
