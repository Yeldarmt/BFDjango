# Generated by Django 2.0 on 2020-02-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200203_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='sur_name',
        ),
    ]
