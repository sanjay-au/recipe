# Generated by Django 5.0.3 on 2024-03-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipes_ingr'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]