# Generated by Django 3.1.1 on 2020-10-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('Recipes', '0003_delete_comment'), ('Recipes', '0004_auto_20201003_1956'), ('Recipes', '0005_auto_20201003_1957'), ('Recipes', '0006_auto_20201003_1957')]

    dependencies = [
        ('Recipes', '0002_auto_20200921_0034'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prepare_dish_recipe',
            field=models.TextField(max_length=2000),
        ),
    ]