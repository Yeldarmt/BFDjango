from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from todo_project.main.views import TodoListAPiView, TodoDetailAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('todo_list/', TodoListAPiView.as_view()),
    path('todo_list/<int:pk>/', TodoDetailAPIView.as_view()),
]
