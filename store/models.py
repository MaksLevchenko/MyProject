from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    slug = models.SlugField(unique=True, max_length=20, verbose_name='слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=35, verbose_name='наименование')
    image = models.ImageField(verbose_name='изображение', upload_to='product/')
    description = models.TextField(max_length=200, verbose_name='описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    slug = models.SlugField(unique=True, max_length=20, verbose_name='слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class UserProductFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    like = models.BooleanField(default=False, verbose_name='Лайк')
    is_favorites = models.BooleanField(default=False, verbose_name='Избранное')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


