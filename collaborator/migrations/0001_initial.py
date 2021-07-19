# Generated by Django 3.1 on 2021-07-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(choices=[(1, 'Project Admin'), (2, 'Project Manager'), (3, 'Project Leader'), (4, 'Member'), (5, 'Custom')], default=4)),
                ('is_active', models.BooleanField(default=True, verbose_name='invite_active')),
                ('status', models.CharField(choices=[('Invited', 'Onhold'), ('Joined', 'Joined'), ('Leave', 'Leaved'), ('Declined', 'Declined')], default='Invited', max_length=120, verbose_name='invite status')),
            ],
            options={
                'verbose_name': 'Collaborator',
                'verbose_name_plural': 'Collaborators',
            },
        ),
    ]
