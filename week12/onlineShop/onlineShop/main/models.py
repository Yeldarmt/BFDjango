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
