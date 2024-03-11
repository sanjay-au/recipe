# Generated by Django 5.0.3 on 2024-03-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipes_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='cuisine',
            field=models.CharField(choices=[('Indian', 'Indian'), ('Chinese', 'Chinese'), ('Italian', 'Italian')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='meal_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='', max_length=20),
        ),
    ]
