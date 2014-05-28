# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Variety'
        db.create_table(u'catalog_variety', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'catalog', ['Variety'])

        # Adding model 'Distillery'
        db.create_table(u'catalog_distillery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'catalog', ['Distillery'])

        # Adding model 'Whisky'
        db.create_table(u'catalog_whisky', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('variety', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Variety'])),
            ('distillery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Distillery'])),
        ))
        db.send_create_signal(u'catalog', ['Whisky'])


    def backwards(self, orm):
        # Deleting model 'Variety'
        db.delete_table(u'catalog_variety')

        # Deleting model 'Distillery'
        db.delete_table(u'catalog_distillery')

        # Deleting model 'Whisky'
        db.delete_table(u'catalog_whisky')


    models = {
        u'catalog.distillery': {
            'Meta': {'object_name': 'Distillery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'catalog.variety': {
            'Meta': {'object_name': 'Variety'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'catalog.whisky': {
            'Meta': {'object_name': 'Whisky'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'distillery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Distillery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Variety']"})
        }
    }

    complete_apps = ['catalog']