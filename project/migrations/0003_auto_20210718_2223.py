# Generated by Django 3.1 on 2021-07-18 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20210718_2223'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collaborator', '0001_initial'),
        ('project', '0002_auto_20210718_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='members',
        ),
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(default=[0], through='collaborator.Collaborator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='activities',
            field=models.ManyToManyField(blank=True, related_name='activity', to='activity.Activity', verbose_name='activity'),
        ),
        migrations.DeleteModel(
            name='ProjectMember',
        ),
    ]
