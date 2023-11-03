# Generated by Django 4.2.5 on 2023-11-03 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categor', models.CharField(blank=True, max_length=100)),
                ('slug', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('content', models.TextField()),
                ('data_create', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='blog_img/')),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('categor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categor_post', to='blog.category')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]