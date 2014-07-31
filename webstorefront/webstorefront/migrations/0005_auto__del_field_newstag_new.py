# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field tags on 'New'
        m2m_table_name = db.shorten_name('webstorefront_new_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('new', models.ForeignKey(orm['webstorefront.new'], null=False)),
            ('newstag', models.ForeignKey(orm['webstorefront.newstag'], null=False))
        ))
        #db.create_unique(m2m_table_name, ['new_id', 'newstag_id'])

        # Deleting field 'NewsTag.new'
        #db.delete_column('webstorefront_newstag', 'new_id')


    def backwards(self, orm):
        # Removing M2M table for field tags on 'New'
        db.delete_table(db.shorten_name('webstorefront_new_tags'))


        # User chose to not deal with backwards NULL issues for 'NewsTag.new'
        raise RuntimeError("Cannot reverse this migration. 'NewsTag.new' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'NewsTag.new'
        db.add_column('webstorefront_newstag', 'new',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstorefront.New'], related_name='tags'),
                      keep_default=False)


    models = {
        'webstorefront.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'305dcdce-bff9-4e43-a8fe-4c6f8bf64b9c'", 'max_length': '140'})
        },
        'webstorefront.new': {
            'Meta': {'object_name': 'New'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_reg': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['webstorefront.NewsTag']", 'symmetrical': 'False', 'related_name': "'news'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'2303159a-bd89-4071-83cf-7aedf9805564'", 'max_length': '140'})
        },
        'webstorefront.newstag': {
            'Meta': {'object_name': 'NewsTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'webstorefront.ware': {
            'Meta': {'object_name': 'Ware'},
            'catalog': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['webstorefront.Catalog']", 'symmetrical': 'False', 'related_name': "'wares'"}),
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'1ad0b2ba-f1d4-4281-9e09-fe4841874a31'", 'max_length': '140'})
        }
    }

    complete_apps = ['webstorefront']