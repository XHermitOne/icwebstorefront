# -*- coding: utf-8 -*-

import uuid
import os.path
import datetime

from django.db import models
from django.conf import settings

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.datetime.now


def image_file_path(instance=None, filename=None, size=None, ext=None):
    """
    Функция определения пути файла образа.
    """
    img_path = settings.IMAGE_STORAGE_DIR
    img_filename = instance.uuid+'.jpg'
    return os.path.join(img_path, img_filename)


class Catalog(models.Model):
    """
    Каталог товаров.
    """
    uuid = models.CharField(max_length=140,
                            default=lambda: str(uuid.uuid4()))

    label = models.CharField(max_length=200)

    def __unicode__(self):
        return self.label


class Ware(models.Model):
    """
    Товар.
    """
    uuid = models.CharField(max_length=140,
                            default=lambda: str(uuid.uuid4()))

    label = models.CharField(max_length=200)
    price = models.FloatField()
    img = models.ImageField(upload_to=image_file_path)
    catalog = models.ManyToManyField(Catalog, related_name='wares')
    count = models.PositiveIntegerField()

    def __unicode__(self):
        return self.label


class NewsTag(models.Model):
    """
    Тэг.
    """
    label = models.CharField(max_length=100)

    def __unicode__(self):
        return self.label


class New(models.Model):
    """
    Новость.
    """
    uuid = models.CharField(max_length=140, default=lambda: str(uuid.uuid4()))
    title = models.CharField(max_length=300)
    body = models.TextField()
    date_reg = models.DateTimeField(default=now)
    tags = models.ManyToManyField(NewsTag, related_name='news', null=True)

    def __unicode__(self):
        return self.title


class Order(models.Model):
    """
    Заказ.
    """
    uuid = models.CharField(max_length=140, default=lambda: str(uuid.uuid4()))
    address = models.TextField()
    date_create = models.DateTimeField(default=now)


class OrderPos(models.Model):
    """
    Позиция заказа.
    """
    ware_uuid = models.CharField(max_length=140, null=True)
    count = models.PositiveIntegerField()
    summ = models.FloatField()
    order = models.ForeignKey(Order, related_name='positions')

