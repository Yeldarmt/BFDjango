from rest_framework import generics, mixins
from todo_project.main.models import Todo
from todo_project.main.serializers import TodoSerializer


class TodoListAPiView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

