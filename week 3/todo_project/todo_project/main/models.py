from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    pass


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return 'Todo id: {}, title: {}'.format(self.id, self.title)
