from django.contrib.auth import get_user_model
from django.db import models
from shoopelectonic.models import Products


# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='cart_product', blank=True, )
    data_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата покупки')
    quantitu = models.IntegerField(default=1, verbose_name='Колличество')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None,
                             related_name='user_cart',
                             verbose_name='Пользователь')

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Order(models.Model):
    STATUS = [
        ('DE', 'В доставке'),
        ('DR', 'Доставлен'),
        ('SR', 'Завершен')
    ]

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилиф')
    company = models.CharField(max_length=70, blank=True, verbose_name='Имя Компании')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='адрес')
    postcode = models.CharField(max_length=30, blank=True, verbose_name='Код почты')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    comment = models.TextField(blank=True, verbose_name='Комментарий к заказу')
    price = models.IntegerField(blank=True, null=True, verbose_name='Сумма заказа')
    status = models.CharField(max_length=2, choices=STATUS, default='DE', verbose_name='Статус')
    data_create = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата заказа')

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='заказчик')
    product = models.ManyToManyField(Products, blank=True, verbose_name='Товары в заказе')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

