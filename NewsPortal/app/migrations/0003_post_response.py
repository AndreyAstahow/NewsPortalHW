# Generated by Django 5.0 on 2023-12-19 21:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_category_alter_post_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='response',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
