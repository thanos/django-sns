'''
Created on July, 15th 2013


@author: thanos
'''
import django.dispatch

sns_signal = django.dispatch.Signal(providing_args=["type", "message_id"])