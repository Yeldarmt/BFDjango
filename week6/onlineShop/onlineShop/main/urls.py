from django.urls import path
from onlineShop.main.views import CategoryDetailApiView, CategoryListApiView, ProductsApiView

urlpatterns = [
    path('categories/', CategoryListApiView.as_view()),
    path('categories/<int:pk>/', CategoryDetailApiView.as_view()),
    path('categories/<int:pk>/products/', ProductsApiView.as_view())
]
