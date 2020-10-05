# Generated by Django 3.1.1 on 2020-10-03 20:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0002_auto_20201003_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(10, message='Your comment had to have at least 10 characters')]),
        ),
    ]