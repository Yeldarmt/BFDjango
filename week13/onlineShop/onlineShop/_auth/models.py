from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    USER_ROLES = (
        (1, 'admin'),
        (2, 'moderator'),
        (3, 'editor'),
    )
    is_staff = models.BooleanField(default=False)
    role = models.IntegerField(choices=USER_ROLES, default=1)

    # role = models.ManyToManyField(Role)
    # class Role(models.Model):
    #     name = models.CharField(max_length=200)
    #     # permissions
    #
    #
    # class UserRole(models.Model):
    #     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    #     role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'

    def __str__(self):
        return '{}, : {}'.format(self.id, self.username)
