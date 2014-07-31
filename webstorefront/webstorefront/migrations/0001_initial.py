# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Catalog'
        db.create_table('webstorefront_catalog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=140, default='91f6873b-6df7-42de-9d67-c0645f4c4f7c')),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('webstorefront', ['Catalog'])

        # Adding model 'Ware'
        db.create_table('webstorefront_ware', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=140, default='2c542b1b-aaa6-4b04-83e3-8d6ff7369bc4')),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('webstorefront', ['Ware'])

        # Adding M2M table for field catalog on 'Ware'
        m2m_table_name = db.shorten_name('webstorefront_ware_catalog')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ware', models.ForeignKey(orm['webstorefront.ware'], null=False)),
            ('catalog', models.ForeignKey(orm['webstorefront.catalog'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ware_id', 'catalog_id'])

        # Adding model 'New'
        db.create_table('webstorefront_new', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=140, default='ccf1ec15-65b5-4bf7-b073-0be997d1b7c7')),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('webstorefront', ['New'])

        # Adding model 'NewsTag'
        db.create_table('webstorefront_newstag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('webstorefront', ['NewsTag'])


    def backwards(self, orm):
        # Deleting model 'Catalog'
        db.delete_table('webstorefront_catalog')

        # Deleting model 'Ware'
        db.delete_table('webstorefront_ware')

        # Removing M2M table for field catalog on 'Ware'
        db.delete_table(db.shorten_name('webstorefront_ware_catalog'))

        # Deleting model 'New'
        db.delete_table('webstorefront_new')

        # Deleting model 'NewsTag'
        db.delete_table('webstorefront_newstag')


    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'36987bff-c5e2-444e-880a-c1fd01ea5b4b'"})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'d6ee678d-7ab6-42db-a734-3f5120f5e9d4'"})
        },
        'webstorefront.newstag': {
            'Meta': {'object_name': 'NewsTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wares'", 'symmetrical': 'False', 'to': "orm['webstorefront.Catalog']"}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'d8b8b6f3-d9d6-4807-81ad-56871bfca500'"})
        }
    }

    complete_apps = ['webstorefront']