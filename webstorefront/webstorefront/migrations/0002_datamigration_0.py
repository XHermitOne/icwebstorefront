# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import uuid
import os.path

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        #Добавить каталог
        if orm.icCatalog.objects.all().count() == 0:
            catalog_data = [u'Пицца',
                            u'Салаты',
                            u'Закуски',
                            u'Напитки',
                            u'Десерты']
            pizza_data = [
                ('2fd235bc-8854-4331-8b7e-e2094154b186', u'Халапеньо', 400, '/home/xhermit/dev/prj/freelance/icwebstorefront/icwebstorefront/webstorefront/media/images/2fd235bc-8854-4331-8b7e-e2094154b186.jpg', 1),
                ('325381cb-b1ab-4d41-8e21-7d6cd4202c55', u'Пепперони', 450.5, '/home/xhermit/dev/prj/freelance/icwebstorefront/icwebstorefront/webstorefront/media/images/325381cb-b1ab-4d41-8e21-7d6cd4202c55.jpg', 1),
                ('850c8166-4b20-4336-8158-2b40fb0bd9d2', u'С грибами и шпинатом', 350, '/home/xhermit/dev/prj/freelance/icwebstorefront/icwebstorefront/webstorefront/media/images/850c8166-4b20-4336-8158-2b40fb0bd9d2.jpg', 1),
                ('a3a3da3e-27b5-4e0c-9f51-605677bee5e2', u'Вегетарианская', 340, '/home/xhermit/dev/prj/freelance/icwebstorefront/icwebstorefront/webstorefront/media/images/a3a3da3e-27b5-4e0c-9f51-605677bee5e2.jpg', 2),
                ('fee75a92-69ad-45c6-bf28-142bc156f1cd', u'Белая', 340, '/home/xhermit/dev/prj/freelance/icwebstorefront/icwebstorefront/webstorefront/media/images/fee75a92-69ad-45c6-bf28-142bc156f1cd.jpg', 3),
                ('f4ca4fc8-81d9-4296-ad17-701e38a03274', u'Барбекю', 370, '/home/xhermit/dev/prj/freelance/icwebstorefront/icwebstorefront/webstorefront/media/images/f4ca4fc8-81d9-4296-ad17-701e38a03274.jpg', 7),
            ]
            salat_data = [
                (uuid.uuid4(), u'Салат "Наполи"', 200, None, 1),
                (uuid.uuid4(), u'Салат Коул-слоу', 200, None, 1),
                (uuid.uuid4(), u'Салат из свежих помидоров и огурцов', 200, None, 1),
            ]
            food_data = [
                (uuid.uuid4(), u'Лазанья мясная', 270, None, 1),
                (uuid.uuid4(), u'Наггетсы куриные', 300, None, 1),
            ]
            water_data = [
                (uuid.uuid4(), u'Аква минерале', 50, None, 1),
            ]
            desert_data = [
                (uuid.uuid4(), u'Мороженое Баскин-Роббинс', 100, None, 1),
            ]

            wares_data = [pizza_data, salat_data, food_data, water_data, desert_data]

            for i, catalog_name in enumerate(catalog_data):
                new_catalog = orm.icCatalog(label=catalog_name, uuid=uuid.uuid4())
                new_catalog.save()

                for ware in wares_data[i]:
                    img_filename = ware[3]
                    if not img_filename or not os.path.exists(img_filename):
                        img_filename = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                                    'media/images/no_image.jpg')
                    new_ware = orm.icWare(label=ware[1], uuid=ware[0], price=ware[2], img=img_filename,
                                          count=ware[4])
                    new_ware.save()
                    new_ware.catalog.add(new_catalog)

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'webstorefront.iccatalog': {
            'Meta': {'object_name': 'icCatalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'45b476ab-1a89-4c8b-9248-ec0a3eb4ad4d'", 'max_length': '140'})
        },
        'webstorefront.icware': {
            'Meta': {'object_name': 'icWare'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wares'", 'symmetrical': 'False', 'to': "orm['webstorefront.icCatalog']"}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'441d374c-4b98-4499-a5ae-8fa5f6f3fa08'", 'max_length': '140'})
        }
    }

    complete_apps = ['webstorefront']
    symmetrical = True
