from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('time/<int:pk>/', views.time)
]
