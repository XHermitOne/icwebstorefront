# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OrderPos.ware_uuid'
        db.add_column('webstorefront_orderpos', 'ware_uuid',
                      self.gf('django.db.models.fields.CharField')(max_length=140, null=True),
                      keep_default=False)

        # Removing M2M table for field ware on 'OrderPos'
        db.delete_table(db.shorten_name('webstorefront_orderpos_ware'))


    def backwards(self, orm):
        # Deleting field 'OrderPos.ware_uuid'
        db.delete_column('webstorefront_orderpos', 'ware_uuid')

        # Adding M2M table for field ware on 'OrderPos'
        m2m_table_name = db.shorten_name('webstorefront_orderpos_ware')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orderpos', models.ForeignKey(orm['webstorefront.orderpos'], null=False)),
            ('ware', models.ForeignKey(orm['webstorefront.ware'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orderpos_id', 'ware_id'])


    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'1f0d5bde-5db1-4a4d-a35b-384eb82a47ac'"})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_reg': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'news'", 'to': "orm['webstorefront.NewsTag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'d9eaab0d-f6f9-47ee-aa29-0922531fb34a'"})
        },
        'webstorefront.newstag': {
            'Meta': {'object_name': 'NewsTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'webstorefront.order': {
            'Meta': {'object_name': 'Order'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'date_create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'ee6826ce-9d17-4954-b1a2-57081c102877'"})
        },
        'webstorefront.orderpos': {
            'Meta': {'object_name': 'OrderPos'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': "orm['webstorefront.Order']"}),
            'summ': ('django.db.models.fields.FloatField', [], {}),
            'ware_uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True'})
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wares'", 'to': "orm['webstorefront.Catalog']", 'symmetrical': 'False'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'324cd8b5-c93e-4023-b3b9-11c1abf562e3'"})
        }
    }

    complete_apps = ['webstorefront']