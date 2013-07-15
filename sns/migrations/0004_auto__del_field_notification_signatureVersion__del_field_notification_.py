# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Notification.signatureVersion'
        db.delete_column(u'sns_notification', 'signatureVersion')

        # Deleting field 'Notification.signature'
        db.delete_column(u'sns_notification', 'signature')

        # Deleting field 'Notification.subscribeURL'
        db.delete_column(u'sns_notification', 'subscribeURL')

        # Deleting field 'Notification.signingCertURL'
        db.delete_column(u'sns_notification', 'signingCertURL')

        # Deleting field 'Notification.UnsubscribeURL'
        db.delete_column(u'sns_notification', 'UnsubscribeURL')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Notification.signatureVersion'
        raise RuntimeError("Cannot reverse this migration. 'Notification.signatureVersion' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Notification.signature'
        raise RuntimeError("Cannot reverse this migration. 'Notification.signature' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Notification.subscribeURL'
        raise RuntimeError("Cannot reverse this migration. 'Notification.subscribeURL' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Notification.signingCertURL'
        raise RuntimeError("Cannot reverse this migration. 'Notification.signingCertURL' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Notification.UnsubscribeURL'
        raise RuntimeError("Cannot reverse this migration. 'Notification.UnsubscribeURL' and its values cannot be restored.")

    models = {
        u'sns.notification': {
            'Meta': {'object_name': 'Notification'},
            'errors': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'messageId': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '9'}),
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