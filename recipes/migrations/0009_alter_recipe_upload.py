# Generated by Django 4.0.2 on 2022-04-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='upload',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
        ),
    ]
