# Generated by Django 3.1 on 2021-07-18 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
        ('project', '0001_initial'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='project',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tasks',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks', to='task.Task', verbose_name='task'),
        ),
    ]
