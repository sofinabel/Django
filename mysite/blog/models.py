from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано в')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено в')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_articles', kwargs={"article_id": self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории', db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
