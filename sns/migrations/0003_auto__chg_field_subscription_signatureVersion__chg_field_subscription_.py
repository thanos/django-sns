# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Subscription.signatureVersion'
        db.alter_column(u'sns_subscription', 'signatureVersion', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Subscription.subscribeURL'
        db.alter_column(u'sns_subscription', 'subscribeURL', self.gf('django.db.models.fields.URLField')(max_length=512, null=True))

        # Changing field 'Subscription.token'
        db.alter_column(u'sns_subscription', 'token', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Subscription.signingCertURL'
        db.alter_column(u'sns_subscription', 'signingCertURL', self.gf('django.db.models.fields.URLField')(max_length=512, null=True))

        # Changing field 'Subscription.signature'
        db.alter_column(u'sns_subscription', 'signature', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Subscription.signatureVersion'
        raise RuntimeError("Cannot reverse this migration. 'Subscription.signatureVersion' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Subscription.subscribeURL'
        raise RuntimeError("Cannot reverse this migration. 'Subscription.subscribeURL' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Subscription.token'
        raise RuntimeError("Cannot reverse this migration. 'Subscription.token' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Subscription.signingCertURL'
        raise RuntimeError("Cannot reverse this migration. 'Subscription.signingCertURL' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Subscription.signature'
        raise RuntimeError("Cannot reverse this migration. 'Subscription.signature' and its values cannot be restored.")

    models = {
        u'sns.notification': {
            'Meta': {'object_name': 'Notification'},
            'UnsubscribeURL': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'errors': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'messageId': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'signatureVersion': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'signingCertURL': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '9'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'subscribeURL': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
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