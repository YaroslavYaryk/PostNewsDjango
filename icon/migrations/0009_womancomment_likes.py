# Generated by Django 3.2.5 on 2021-08-16 19:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icon', '0008_remove_womanlike_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='womancomment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='com_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
