from django.urls import path
from main import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'todos', views.TodoViewSet)

urlpatterns = router.urls
