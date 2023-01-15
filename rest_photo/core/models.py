from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     login = models.CharField(max_length=255, verbose_name='Логин')
#     password = models.CharField(max_length=255, verbose_name='Пароль')
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         ordering = ('login',)


class Photo(models.Model):
    people = models.CharField(max_length = 255, default='Нет людей на фото', verbose_name='Люди на фото')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images/", default='-', verbose_name='Фото')
    location = models.TextField(max_length=255, verbose_name='Гео-локация')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, verbose_name='Время создания')
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ('location',)


