# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Notification.state'
        db.delete_column(u'sns_notification', 'state')

        # Adding field 'Notification.status'
        db.add_column(u'sns_notification', 'status',
                      self.gf('django.db.models.fields.CharField')(default='PENDING', max_length=9),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Notification.state'
        db.add_column(u'sns_notification', 'state',
                      self.gf('django.db.models.fields.CharField')(default='PENDING', max_length=9),
                      keep_default=False)

        # Deleting field 'Notification.status'
        db.delete_column(u'sns_notification', 'status')


    models = {
        u'sns.notification': {
            'Meta': {'object_name': 'Notification'},
            'errors': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'messageId': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '9'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'topicArn': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'sns.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'errors': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'messageId': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'signatureVersion': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'signingCertURL': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '7'}),
            'subscribeURL': ('django.db.models.fields.URLField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'topicArn': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['sns']