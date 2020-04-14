from rest_framework import mixins, viewsets
from onlineShop.api.models import Product
from onlineShop.api.serializers import ProductShortSerializer, ProductFullSerializer


class ProductListViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin
                         ):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductShortSerializer
        if self.action == 'retrieve':
            return ProductFullSerializer
        return ProductShortSerializer

