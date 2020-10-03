# Generated by Django 3.1.1 on 2020-10-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0003_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='prepare_dish_recipe',
            field=models.TextField(default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
