# -*- coding: utf-8 -*-

import uuid
import os.path

from django.db import models
from django.conf import settings

class icCatalog(models.Model):
    """
    Каталог товаров.
    """
    uuid = models.CharField(max_length=140,
                            default=lambda: str(uuid.uuid4()))

    #parent = models.OneToOneField(icCatalog)
    #children = models.OneToManyField(icCatalog)
    label = models.CharField(max_length=200)

    def __unicode__(self):
        return self.label

def image_file_path(instance=None, filename=None, size=None, ext=None):
    """
    Функция определения пути файла образа.
    """
    img_path = settings.IMAGE_STORAGE_DIR
    img_filename = instance.uuid+'.jpg'
    return os.path.join(img_path, img_filename)

class icWare(models.Model):
    """
    Товар.
    """
    uuid = models.CharField(max_length=140,
                            default=lambda: str(uuid.uuid4()))

    label = models.CharField(max_length=200)
    price = models.FloatField()
    img = models.ImageField(upload_to=image_file_path)
    catalog = models.ManyToManyField(icCatalog, related_name='wares')
    count = models.PositiveIntegerField()

    def __unicode__(self):
        return self.label

