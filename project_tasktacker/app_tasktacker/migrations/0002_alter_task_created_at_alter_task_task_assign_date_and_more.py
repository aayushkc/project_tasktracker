# Generated by Django 4.0.6 on 2022-07-31 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasktacker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 31, 16, 8, 4, 622244)),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_assign_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_assign_to',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
