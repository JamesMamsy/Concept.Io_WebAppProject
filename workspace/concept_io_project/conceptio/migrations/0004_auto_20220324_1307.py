# Generated by Django 2.2.26 on 2022-03-24 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conceptio', '0003_auto_20220323_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.ManyToManyField(related_name='project_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
