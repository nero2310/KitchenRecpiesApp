# Generated by Django 3.1.1 on 2020-10-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0005_recipe_times_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='prepare_dish_recipe',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
