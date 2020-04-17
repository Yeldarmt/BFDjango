from rest_framework import mixins, generics
from onlineShop.main.models import Category
from onlineShop.main.serializers import CategorySerializer
from onlineShop.api.serializers import ProductShortSerializer
from django.http import Http404
import logging

logger = logging.getLogger('main')


class CategoryListApiView(generics.GenericAPIView,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = ()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Category created, {serializer.instance}')
        logger.info(f'Category created, {serializer.instance}')
        logger.warning(f'Category created, {serializer.instance}')
        logger.error(f'Category created, {serializer.instance}')
        logger.critical(f'Category created, {serializer.instance}')


class CategoryDetailApiView(generics.GenericAPIView,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = ()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductsApiView(generics.GenericAPIView, mixins.ListModelMixin):
    def get_queryset(self):
        try:
            category = Category.objects.get(id=self.kwargs.get('pk'))
            return category.products.all()
        except Category.DoesNotExist:
            return Http404
    serializer_class = ProductShortSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)