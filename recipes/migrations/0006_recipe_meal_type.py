# Generated by Django 3.2.12 on 2022-04-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(choices=[('BR', 'Breakfast'), ('LU', 'Lunch'), ('DI', 'Dinner'), ('SN', 'Snack'), ('OT', 'Other')], default='OT', max_length=2),
        ),
    ]
