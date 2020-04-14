from django.shortcuts import render
from rest_framework import mixins, viewsets
from main.models import Todo
from main.serializers import TodoShortSerializer, TodoFullSerializer


class TodoViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TodoFullSerializer
        return TodoShortSerializer

    queryset = Todo.objects.all()
