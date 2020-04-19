import logging
from rest_framework import mixins, viewsets
from main.models import Todo
from main.serializers import TodoShortSerializer, TodoFullSerializer

logger = logging.getLogger(__name__)


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

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Todo object created, {serializer.instance}')
        logger.info(f'Todo object created, {serializer.instance}')
        logger.warning(f'Todo object created, {serializer.instance}')
        logger.error(f'Todo object created, {serializer.instance}')
        logger.critical(f'Todo object created, {serializer.instance}')
