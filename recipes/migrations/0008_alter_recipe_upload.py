# Generated by Django 4.0.2 on 2022-04-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='upload',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
