from rest_framework import serializers
from onlineShop.main.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    category_desc = serializers.FileField(required=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category_desc = validated_data.get('category_desc', instance.category_desc)
        instance.save()
        return instance

    def validate(self, attrs):
        return attrs

# class CategorySerializer(serializers.ModelSerializer):
#     category_desc = serializers.FileField()
#
#     class Meta:
#         modal = Category
#         fields = ('id', 'name', 'category_desc')
