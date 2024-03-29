from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.description})"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_date = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')
    uploaded_at = models.DateTimeField(**NULLABLE, auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        return f"{self.name}({self.description}). Цена {self.price}"

    class Meta:
        permissions = [
            ('cancel_publish', 'Can cancel product publication'),
            ('can_change_description', 'Can change product description'),
            ('can_change_category', 'Can change product category'),
        ]
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='Слаг', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    public_sign = models.BooleanField(verbose_name='Признак публикации', default=False)
    views_number = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f"{self.title}. Просмотры - {self.views_number}. Опубликовано - {self.created_at}"

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'


class Version(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак версии')

    def __str__(self):
        return f"{self.product} {self.version_name} - {self.version_number}"

    class Meta:

        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
