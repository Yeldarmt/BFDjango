from django.db import models
import os
from django.core.exceptions import ValidationError

ALLOWED_EXTENSIONS = ['.docx', '.pdf']


def validate_extension(value):
    split_ext = os.path.splitext(value.name)
    print('split_ext', split_ext)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file, valid extensions: {ALLOWED_EXTENSIONS}')


class Category(models.Model):
    name = models.CharField(max_length=300)
    category_desc = models.FileField(upload_to='desc_files',
                                     validators=[validate_extension],
                                     null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return 'Category id: {}, name: {}'.format(self.id, self.name)

    def _try_create_profile_for_user(self, created):
        print('not in _try_create_profile_for_user')
        if created:
            print('in _try_create_profile_for_user')
            CategoryFullInfo.objects.get_or_create(category=self)

    def save(self, *args, **kwargs):
        print('before saving')

        created = self.id is None

        self.name = f'main_{self.name}'

        super(Category, self).save(*args, **kwargs)

        self._try_create_profile_for_user(created)

        print('after saving')


class CategoryFullInfo(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    category_info = models.TextField(default='')
