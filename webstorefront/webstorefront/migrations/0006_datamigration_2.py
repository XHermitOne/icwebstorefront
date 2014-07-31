# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

import random


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        #Добавить новости

        for i in range(1000):
            title = u'Новость № %d' % i
            body = u'Текст '*20

            new_new = orm.New(title=title, body=body)
            new_new.save()
            for i_tag in range(int(random.random()*10)):
                tag = orm.NewsTag.objects.all()[i_tag]
                tag.news.add(new_new)
                new_new.tags.add(tag)
            new_new.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'2dbaa16b-7324-4409-8cf0-8e1b34f89d90'"})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_reg': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['webstorefront.NewsTag']", 'related_name': "'news'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'93f1ab06-47e2-41b4-8c13-d3d2524c1440'"})
        },
        'webstorefront.newstag': {
            'Meta': {'object_name': 'NewsTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['webstorefront.Catalog']", 'related_name': "'wares'"}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'84e8f0da-dbb1-4d10-9bd5-d153449c3a8b'"})
        }
    }

    complete_apps = ['webstorefront']
    symmetrical = True
