# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table('website_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('initial_image', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('website', ['Blog'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('website_blog')


    models = {
        'website.blog': {
            'Meta': {'object_name': 'Blog'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_image': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['website']