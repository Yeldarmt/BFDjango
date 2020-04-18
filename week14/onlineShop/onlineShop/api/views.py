from rest_framework import mixins, viewsets
from onlineShop.api.models import Product
from onlineShop.api.serializers import ProductShortSerializer, ProductFullSerializer
import logging

logger = logging.getLogger('main')


class ProductListViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin
                         ):
    def get_queryset(self):
        if self.action == 'list':
            return Product.objects.select_related('category')
        return Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductShortSerializer
        if self.action == 'retrieve':
            return ProductFullSerializer
        return ProductShortSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Product created, {serializer.instance}')
        logger.info(f'Product created, {serializer.instance}')
        logger.warning(f'Product created, {serializer.instance}')
        logger.error(f'Product created, {serializer.instance}')
        logger.critical(f'Product created, {serializer.instance}')

