# Generated by Django 3.1.1 on 2020-09-21 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='Comments',
        ),
    ]