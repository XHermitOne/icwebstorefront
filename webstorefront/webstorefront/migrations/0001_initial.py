# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'icCatalog'
        db.create_table('webstorefront_iccatalog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=140, default='3216ed70-6042-46d1-b47e-127291801eda')),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('webstorefront', ['icCatalog'])

        # Adding model 'icWare'
        db.create_table('webstorefront_icware', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=140, default='aa593ef4-9beb-4bd3-a2dd-bd2132f4f85b')),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('webstorefront', ['icWare'])

        # Adding M2M table for field catalog on 'icWare'
        m2m_table_name = db.shorten_name('webstorefront_icware_catalog')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('icware', models.ForeignKey(orm['webstorefront.icware'], null=False)),
            ('iccatalog', models.ForeignKey(orm['webstorefront.iccatalog'], null=False))
        ))
        db.create_unique(m2m_table_name, ['icware_id', 'iccatalog_id'])


    def backwards(self, orm):
        # Deleting model 'icCatalog'
        db.delete_table('webstorefront_iccatalog')

        # Deleting model 'icWare'
        db.delete_table('webstorefront_icware')

        # Removing M2M table for field catalog on 'icWare'
        db.delete_table(db.shorten_name('webstorefront_icware_catalog'))


    models = {
        'webstorefront.iccatalog': {
            'Meta': {'object_name': 'icCatalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'5023354a-c79c-4110-b631-e1c9d8721824'"})
        },
        'webstorefront.icware': {
            'Meta': {'object_name': 'icWare'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['webstorefront.icCatalog']", 'related_name': "'wares'", 'symmetrical': 'False'}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'66b87152-7469-4853-84e0-f433d39e0b46'"})
        }
    }

    complete_apps = ['webstorefront']