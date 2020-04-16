from rest_framework.routers import DefaultRouter
from onlineShop.api.views import ProductListViewSet

router = DefaultRouter()

router.register(r'products', ProductListViewSet)

urlpatterns = router.urls
