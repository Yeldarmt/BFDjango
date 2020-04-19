from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


class TodoManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(created_by=user)


class CompletedTodoManager(models.Manager):
    def get_queryset(self):
        return super(CompletedTodoManager, self).get_queryset().filter(completed=True)


class MyUser(AbstractUser):
    def _try_create_profile_for_user(self, created):
        print('not in _try_create_profile_for_user')
        if created:
            print('in _try_create_profile_for_user')
            Profile.objects.get_or_create(user=self)

    def save(self, *args, **kwargs):
        print('before saving')

        created = self.id is None

        self.username = f'main_{self.username}'

        super(MyUser, self).save(*args, **kwargs)

        self._try_create_profile_for_user(created)

        print('after saving')


def valid_title(value):
    if '%' in value:
        raise serializers.ValidationError('invalid title')


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    address = models.TextField(default='')


class Todo(models.Model):
    title = models.CharField(max_length=200, validators=[valid_title])
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    objects = TodoManager()
    completed_todos = CompletedTodoManager()

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return 'Todo id: {}, title: {}'.format(self.id, self.title)