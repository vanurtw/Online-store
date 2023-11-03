from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category_name = models.CharField(max_length=40, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacturers(models.Model):
    manufacture_name = models.CharField(max_length=70, verbose_name='Поставщик')

    def __str__(self):
        return self.manufacture_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class ImageProduct(models.Model):
    image = models.ImageField(upload_to='product_img/', verbose_name='Излбражение')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изобажения товаров'


class Products(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Имя товара')
    description = models.TextField(verbose_name='Описние')
    price = models.IntegerField(blank=True, default=0)
    alt_price = models.IntegerField(default=0, verbose_name='Цена')
    img = models.ForeignKey(ImageProduct, on_delete=models.CASCADE, verbose_name='Изображение')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, related_name='categor_product',
                                 verbose_name='Категория')
    manufacture = models.ForeignKey(Manufacturers, on_delete=models.CASCADE, verbose_name='Поставщик')
    sale = models.PositiveIntegerField(default=0, verbose_name='Скидка в процентах')
    besteller = models.BooleanField(default=False, verbose_name='Бестселлер')
    new_product = models.BooleanField(default=True, verbose_name='Новый товар')
    sale_products = models.BooleanField(default=False, verbose_name='Скидка на товар')

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.price = self.price
        if self.sale:
            self.sale_products = True
        self.price = self.alt_price * ((100 - self.sale) / 100)
        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
