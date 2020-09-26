# Generated by Django 3.1.1 on 2020-09-21 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Recipes', '0003_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('up_vote', models.IntegerField(default=0)),
                ('down_vote', models.IntegerField(default=0)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recipes.recipe')),
            ],
            options={
                'db_table': 'Comments',
            },
        ),
    ]