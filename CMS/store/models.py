from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import mptt
from django.core.exceptions import ValidationError


""" Раздел 1. Бренды, категории и товары """


class Brand(models.Model):
    """Бренд"""
    name = models.CharField('название', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'


class Category(MPTTModel):
    """Категория"""
    name = models.CharField('название', max_length=64)
    slug = models.SlugField('человекопонятный url-адрес', max_length=64)
    parent = TreeForeignKey('self', models.CASCADE, blank=True, db_index=True, null=True, related_name='children',
                            verbose_name='родительская категория')

    def clean(self):
        super(Category, self).clean()
        if self.parent is None:
            if Category.objects.filter(slug=self.name).exists():
                raise ValidationError('Корневая категория с таким названием уже существует.')
            if Category.objects.filter(slug=self.slug).exists():
                raise ValidationError('Корневая категория с таким человекопонятным url-адресом уже существует.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        unique_together = (
            ('name', 'parent'),  # уникальность название + родительская
            ('slug', 'parent'),  # уникальность ЧПУ + родительская
        )

    class MPTTMeta:
        order_insertion_by = ['name']

class Product(models.Model):
    """Товар"""
    name = models.CharField('наименование товара', max_length=128, unique=True)
    slug = models.SlugField('человекопонятный url-адрес', max_length=64, unique=True)
    brand = models.ForeignKey(Brand, models.CASCADE, blank=True, null=True, verbose_name='бренд')
    category = TreeForeignKey(Category, models.CASCADE, verbose_name='категория')
    description = RichTextUploadingField('описание товара', blank=True, config_name='default')
    base_price = models.DecimalField('базовая цена', max_digits=8, decimal_places=2, default=0)
    photo = models.ImageField(upload_to='store/products/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        #ordering = ['-base_price']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
