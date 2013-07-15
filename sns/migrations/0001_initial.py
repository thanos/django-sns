# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscription'
        db.create_table(u'sns_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('messageId', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('topicArn', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('subscribeURL', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('signatureVersion', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('signingCertURL', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('status', self.gf('django.db.models.fields.CharField')(default='PENDING', max_length=7)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'sns', ['Subscription'])

        # Adding model 'Notification'
        db.create_table(u'sns_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('messageId', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('topicArn', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('subscribeURL', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('signatureVersion', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('signingCertURL', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('UnsubscribeURL', self.gf('django.db.models.fields.URLField')(max_length=512)),
            ('state', self.gf('django.db.models.fields.CharField')(default='PENDING', max_length=9)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'sns', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Subscription'
        db.delete_table(u'sns_subscription')

        # Deleting model 'Notification'
        db.delete_table(u'sns_notification')


    models = {
        u'sns.notification': {
            'Meta': {'object_name': 'Notification'},
            'UnsubscribeURL': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'messageId': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'signatureVersion': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'signingCertURL': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'PENDING'", 'max_length': '7'}),
            'subscribeURL': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'topicArn': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['sns']