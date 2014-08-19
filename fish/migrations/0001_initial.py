# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TwitterHandle'
        db.create_table(u'fish_twitterhandle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1024)),
        ))
        db.send_create_signal(u'fish', ['TwitterHandle'])

        # Adding model 'Tweet'
        db.create_table(u'fish_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fish.TwitterHandle'])),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('raw_tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('translated_tweet', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fish', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'TwitterHandle'
        db.delete_table(u'fish_twitterhandle')

        # Deleting model 'Tweet'
        db.delete_table(u'fish_tweet')


    models = {
        u'fish.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'translated_tweet': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fish.TwitterHandle']"})
        },
        u'fish.twitterhandle': {
            'Meta': {'object_name': 'TwitterHandle'},
            'handle': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['fish']