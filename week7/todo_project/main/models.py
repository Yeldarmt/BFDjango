from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


class TodoManager(models.Manager):
    def for_user(self, user):
        return self.objects.filter(created_by=user)


class CompletedTodoManager(models.Manager):
    def get_queryset(self):
        return self.filter(completed=True)


class MyUser(AbstractUser):
    pass


def valid_title(value):
    if '%' in value:
        raise serializers.ValidationError('invalid title')


class Todo(models.Model):
    title = models.CharField(max_length=200, validators=[valid_title])
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    objects = TodoManager()
    completed_books = CompletedTodoManager()

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return 'Todo id: {}, title: {}'.format(self.id, self.title)