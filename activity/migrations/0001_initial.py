# Generated by Django 3.1 on 2021-08-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='activity')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Ongoing'), (2, 'On-Hold'), (3, 'Completed'), (4, 'Abolish ')], default=1, verbose_name='status')),
                ('progress', models.SmallIntegerField(blank=True, null=True, verbose_name='overall progress')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
