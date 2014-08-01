# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrderPos'
        db.create_table('webstorefront_orderpos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('summ', self.gf('django.db.models.fields.FloatField')()),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='positions', to=orm['webstorefront.Order'])),
        ))
        db.send_create_signal('webstorefront', ['OrderPos'])

        # Adding M2M table for field ware on 'OrderPos'
        m2m_table_name = db.shorten_name('webstorefront_orderpos_ware')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orderpos', models.ForeignKey(orm['webstorefront.orderpos'], null=False)),
            ('ware', models.ForeignKey(orm['webstorefront.ware'], null=False))
        ))
        db.create_unique(m2m_table_name, ['orderpos_id', 'ware_id'])

        # Adding model 'Order'
        db.create_table('webstorefront_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=140, default='923ac74f-bfb7-4e6b-803b-da5d5e6ce066')),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('date_create', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('webstorefront', ['Order'])


    def backwards(self, orm):
        # Deleting model 'OrderPos'
        db.delete_table('webstorefront_orderpos')

        # Removing M2M table for field ware on 'OrderPos'
        db.delete_table(db.shorten_name('webstorefront_orderpos_ware'))

        # Deleting model 'Order'
        db.delete_table('webstorefront_order')


    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'d7568b8d-45b1-45be-bcd7-9b237a3dc3fd'"})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_reg': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'news'", 'to': "orm['webstorefront.NewsTag']", 'symmetrical': 'False', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'3a3815b6-ffcc-463b-8deb-35b7eac0e4fb'"})
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
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'4d1a0819-205a-49c2-a47a-b4fb4bc489b0'"})
        },
        'webstorefront.orderpos': {
            'Meta': {'object_name': 'OrderPos'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': "orm['webstorefront.Order']"}),
            'summ': ('django.db.models.fields.FloatField', [], {}),
            'ware': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['webstorefront.Ware']", 'symmetrical': 'False'})
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wares'", 'to': "orm['webstorefront.Catalog']", 'symmetrical': 'False'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'5ff75756-d5aa-4d80-9db9-2b908d1f5cb9'"})
        }
    }

    complete_apps = ['webstorefront']