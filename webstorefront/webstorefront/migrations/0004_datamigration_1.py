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

        #Добавить тэги
        for i in range(10):
            new_tag = orm.NewsTag(label=u'Тэг%d' % i)
            new_tag.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'109e8275-f855-41d0-9f34-edb59c19a0b1'"})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_reg': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'9a5d8782-9850-443d-9577-bfc47459b64b'"})
        },
        'webstorefront.newstag': {
            'Meta': {'object_name': 'NewsTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['webstorefront.Catalog']", 'related_name': "'wares'", 'symmetrical': 'False'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'49aab52b-3ccb-4d3e-9dbf-4d4d4e449904'"})
        }
    }

    complete_apps = ['webstorefront']
    symmetrical = True
