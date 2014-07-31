# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.conf import settings

import uuid
import os
import os.path
import shutil
import fnmatch


class Migration(DataMigration):

    def empty_images(self):
        """
        Удалить все образы объектов.
        """
        uuid_jpg_pattern = '????????-????-????-????-????????????.jpg'
        filenames = os.listdir(settings.IMAGE_STORAGE_DIR)
        uuid_jpg_filenames = [os.path.join(settings.IMAGE_STORAGE_DIR, filename)
                              for filename in fnmatch.filter(filenames, uuid_jpg_pattern)]
        for filename in uuid_jpg_filenames:
            os.remove(filename)
            print('Remove file <%s>' % filename)

    def init_images(self, objects):
        """
        Инициализировать образ объекта.
        @param objects: Список данных объектов.
        """
        result =[]
        for obj in objects:
            img_filename = os.path.join(os.path.dirname(__file__), 'images/%s.jpg' % obj[1])
            if os.path.exists(img_filename):
                new_img_filename = os.path.join(settings.IMAGE_STORAGE_DIR, '%s.jpg' % obj[0])
                shutil.copyfile(img_filename, new_img_filename)
                new_obj = list(obj)
                new_obj[3] = new_img_filename
                result.append(tuple(new_obj))
            else:
                result.append(obj)
        return result

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        #Добавить каталог
        if orm.Catalog.objects.all().count() == 0:
            catalog_data = [u'Пицца',
                            u'Салаты',
                            u'Закуски',
                            u'Напитки',
                            u'Десерты']

            self.empty_images()

            pizza_data = [
                (uuid.uuid4(), u'Халапеньо', 400, None, 1),
                (uuid.uuid4(), u'Пепперони', 450.5, None, 1),
                (uuid.uuid4(), u'С грибами и шпинатом', 350, None, 1),
                (uuid.uuid4(), u'Вегетарианская', 340, None, 2),
                (uuid.uuid4(), u'Белая', 340, None, 3),
                (uuid.uuid4(), u'Барбекю', 370, None, 7),
            ]
            pizza_data = self.init_images(pizza_data)

            salat_data = [
                (uuid.uuid4(), u'Салат "Наполи"', 200, None, 1),
                (uuid.uuid4(), u'Салат Коул-слоу', 200, None, 1),
                (uuid.uuid4(), u'Салат из свежих помидоров и огурцов', 200, None, 1),
            ]
            salat_data = self.init_images(salat_data)

            food_data = [
                (uuid.uuid4(), u'Лазанья мясная', 270, None, 1),
                (uuid.uuid4(), u'Наггетсы куриные', 300, None, 1),
            ]
            food_data = self.init_images(food_data)

            water_data = [
                (uuid.uuid4(), u'Аква минерале', 50, None, 1),
            ]
            water_data = self.init_images(water_data)

            desert_data = [
                (uuid.uuid4(), u'Мороженое Баскин-Роббинс', 100, None, 1),
            ]
            desert_data = self.init_images(desert_data)

            wares_data = [pizza_data, salat_data, food_data, water_data, desert_data]

            for i, catalog_name in enumerate(catalog_data):
                new_catalog = orm.Catalog(label=catalog_name, uuid=uuid.uuid4())
                new_catalog.save()

                for ware in wares_data[i]:
                    img_filename = ware[3]
                    if not img_filename or not os.path.exists(img_filename):
                        img_filename = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                                    'media/images/no_image.jpg')
                    new_ware = orm.Ware(label=ware[1], uuid=ware[0], price=ware[2], img=img_filename,
                                        count=ware[4])
                    new_ware.save()
                    new_ware.catalog.add(new_catalog)

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'3d9e1d44-1868-4ba0-ab5f-ec00aaa8503b'", 'max_length': '140'})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'2a45601e-04ec-446c-89e9-9fedcf8c0c9d'", 'max_length': '140'})
        },
        'webstorefront.newstag': {
            'Meta': {'object_name': 'NewsTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wares'", 'to': "orm['webstorefront.Catalog']", 'symmetrical': 'False'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'c31d2dfc-f58a-4a48-9d5c-ae28bc8455ba'", 'max_length': '140'})
        }
    }

    complete_apps = ['webstorefront']
    symmetrical = True
