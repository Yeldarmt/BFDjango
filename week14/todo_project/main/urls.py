from django.urls import path
from main import views
from rest_framework.routers import DefaultRouter
from main.models import Todo


router = DefaultRouter()

router.register(r'todos', views.TodoViewSet, basename=Todo)

urlpatterns = router.urls
