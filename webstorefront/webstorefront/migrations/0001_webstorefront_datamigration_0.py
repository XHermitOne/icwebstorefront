# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

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
            for catalog_name in catalog_data:
                new_catalog = orm.icCatalog(label=catalog_name)
                new_catalog.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'webstorefront.iccatalog': {
            'Meta': {'object_name': 'icCatalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'bf789660-e259-4e04-89e7-5131339f6f4b'", 'max_length': '140'})
        },
        'webstorefront.icware': {
            'Meta': {'object_name': 'icWare'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['webstorefront.icCatalog']"}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'74edc318-e952-4bf1-911d-e38c79a01c04'", 'max_length': '140'})
        }
    }

    complete_apps = ['webstorefront']
    symmetrical = True
