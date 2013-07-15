'''
Created on July, 15th 2013


@author: thanos
'''


import logging, json
logger = logging.getLogger(__name__)


from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import Subscription, Notification

@csrf_exempt
def sns_endpoint(request):
    message = json.loads(request.raw_post_data)
    if message['Type'] == 'SubscriptionConfirmation':
    	obj = Subscription.process(message)
    elif message['Type'] == 'Notification':
    	obj= Notification.add(message)
    else:
    	return HttpResponseBadRequest('Unknown Request')
    return HttpResponse(json.dumps({'status': obj.status, 'message':message}), mimetype="application/json")


def subscribe(request, topic):
    subscription = Subscription.subscribe(topic)
    return HttpResponse(subscription.message, mimetype="application/json")