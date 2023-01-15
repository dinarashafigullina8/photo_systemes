# Generated by Django 4.1.5 on 2023-01-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_photo_people_alter_photo_photo_photo_people'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PeopleOnPhoto',
        ),
        migrations.AlterField(
            model_name='photo',
            name='people',
            field=models.CharField(default='Нет людей на фото', max_length=255, verbose_name='Люди на фото'),
        ),
    ]
