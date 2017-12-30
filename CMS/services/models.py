from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
    """Услуги"""
    name = models.CharField('наименование товара', max_length=128, unique=True)
    slug = models.SlugField('человекопонятный url-адрес', max_length=64, unique=True)
    description = RichTextUploadingField('описание товара', blank=True, config_name='default')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
