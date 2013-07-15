# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2012 by Thanos Vassilakis.

    All rights reserved.
"""

import logging
logger = logging.getLogger(__name__)

from django.contrib import admin

import models


class SubscriptionAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	list_filter = ('status', )
	search_fields = ['topic', 'message', 'messageId']
	list_display = ('topic', 'timestamp', 'status',  'modified')

admin.site.register(models.Subscription, SubscriptionAdmin)


class NotificationAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	list_filter = ('status', 'topicArn')
	search_fields = ['subject', 'message', 'messageId']
	list_display = ('subject', 'topicArn', 'timestamp', 'status',  'modified', 'message')

admin.site.register(models.Notification, NotificationAdmin)