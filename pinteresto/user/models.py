from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.urls import reverse
# Create your models here.


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', blank=True,
                             max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    teg = models.ForeignKey('Tegs', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']


class Views(models.Model):
    title = models.CharField(max_length=20)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.views}'


class Likes(models.Model):
    title = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.likes}'


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField('Комментарий', max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author_name)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-created']


class Tegs(models.Model):
    teg = models.CharField(max_length=255)

    def __str__(self):
        return self.teg

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-teg']


