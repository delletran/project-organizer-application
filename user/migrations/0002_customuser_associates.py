# Generated by Django 3.1 on 2021-07-18 11:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='associates',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='associates'),
        ),
    ]
