from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    categor = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.categor


class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_img/')
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    categor = models.ForeignKey(Category, related_name='categor_post', blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.id})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
