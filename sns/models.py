'''
Created on July, 15th 2013


@author: thanos
'''

import logging, urllib2, datetime, json, traceback
logger = logging.getLogger(__name__)

import boto

from django.db import models

from signals import sns_signal
from django.conf import settings
# Create your models here.


class Subscription(models.Model):
	"""
	{
	"Type" : "SubscriptionConfirmation",
	"MessageId" : "165545c9-2a5c-472c-8df2-7ff2be2b3b1b",
	"Token" : "2336412f37fb687f5d51e6e241d09c805a5a57b30d712f794cc5f6a988666d92768dd60a747ba6f3beb71854e285d6ad02428b09ceece29417f1f02d609c582afbacc99c583a916b9981dd2728f4ae6fdb82efd087cc3b7849e05798d2d2785c03b0879594eeac82c01f235d0e717736",
	"TopicArn" : "arn:aws:sns:us-east-1:123456789012:MyTopic",
	"Message" : "You have chosen to subscribe to the topic arn:aws:sns:us-east-1:123456789012:MyTopic.\nTo confirm the subscription, visit the SubscribeURL included in this message.",
	"SubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-east-1:123456789012:MyTopic&Token=2336412f37fb687f5d51e6e241d09c805a5a57b30d712f794cc5f6a988666d92768dd60a747ba6f3beb71854e285d6ad02428b09ceece29417f1f02d609c582afbacc99c583a916b9981dd2728f4ae6fdb82efd087cc3b7849e05798d2d2785c03b0879594eeac82c01f235d0e717736",
	"Timestamp" : "2012-04-26T20:45:04.751Z",
	"SignatureVersion" : "1",
	"Signature" : "EXAMPLEpH+DcEwjAPg8O9mY8dReBSwksfg2S7WKQcikcNKWLQjwu6A4VbeS0QHVCkhRS7fUQvi2egU3N858fiTDN6bkkOxYDVrY0Ad8L10Hs3zH81mtnPk5uvvolIC1CXGu43obcgFxeL3khZl8IKvO61GWB6jI9b5+gLPoBc1Q=",
	"SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
	}

	"""

	STATUS_ACTIVE = 'ACTIVE'
	STATUS_PENDING= 'PENDING'
	STATUS_RETIRED = 'RETIRED'
	STATUSES =  (STATUS_ACTIVE,STATUS_PENDING, STATUS_RETIRED)

	topic = models.CharField(max_length=128)
	messageId= models.CharField(max_length=48)
	token= models.CharField(max_length=250,null=True, blank=True)
	topicArn = models.CharField(max_length=250)
	message = models.CharField(max_length=250)
	subscribeURL = models.URLField(max_length=512,null=True, blank=True)
	timestamp  = models.DateTimeField()
	signatureVersion = models.CharField(max_length=32, null=True, blank=True)
	signature = models.CharField(max_length=250,null=True, blank=True)
	signingCertURL = models.URLField(max_length=512,null=True, blank=True)
	status = models.CharField(max_length= max(map(len, STATUSES)), choices= zip(STATUSES,map(lambda x: x.capitalize(), STATUSES)), default=STATUS_PENDING) 
	modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	errors =  models.TextField(null=True, blank=True)

	def __unicode__(self):
		return "{} ({}:{})".format(self.topicArn,  self.status, self.modified)

	@classmethod
	def process(cls, message):
		subscription = None
		try:
			topicArn = message['TopicArn']
			subscription = Subscription.objects.get(topicArn=topicArn)
			subscription.messageId = message["MessageId"]
			subscription.token= message["Token"]
			subscription.message = message["Message"]
			subscription.subscribeURL = message["SubscribeURL"]
			subscription.timestamp  = message["Timestamp"]
			subscription.signatureVersion = message["SignatureVersion"]
			subscription.signature = message["Signature"]
			subscription.signingCertURL = message["SigningCertURL"]
			subscription.status = cls.STATUS_ACTIVE
			urllib2.urlopen(message['SubscribeURL']).read()
			subscription.save()
		except:
			if subscription:
				subscription.status = cls.STATUS_ERROR
				subscription.error = traceback.format_exc()
				subscription.save()
			logger.exception("%s( %s )", cls.process, message)
			raise
		return subscription

	
	@classmethod
	def get_topicarn(cls, topic_label):
		response = cls.aws_connection().get_all_topics()
		for topic in response['ListTopicsResponse']['ListTopicsResult']['Topics']:
			if topic['TopicArn'].endswith(topic_label):
				return topic['TopicArn']
	_aws_connection=None
	@classmethod
	def aws_connection(cls):
		if not cls._aws_connection:
			cls._aws_connection = boto.connect_sns(settings.AWS_ACCESS_KEY_ID ,settings.AWS_SECRET_ACCESS_KEY)
		return cls._aws_connection

	@classmethod
	def subscribe(cls, topic_label):
		response = cls.aws_connection().subscribe('arn:aws:sns:us-east-1:062533497915:tweet_filing', 'http', settings.SNS_ENDPOINT)
		'''{u'SubscribeResponse': {u'SubscribeResult': {u'SubscriptionArn': u'pending confirmation'}, u'ResponseMetadata': {u'RequestId': u'01d0e9c4-e566-569b-b9c9-a39aa65e2507'}}}'''
		return Subscription.objects.create(
				topic = topic_label,
				messageId= response['SubscribeResponse']['ResponseMetadata']['RequestId'],
				topicArn = cls.get_topicarn(topic_label),
				message = json.dumps(response),
				timestamp  = datetime.datetime.utcnow(),
				)



class Notification(models.Model):
	"""
	{
	"Type" : "Notification",
	"MessageId" : "22b80b92-fdea-4c2c-8f9d-bdfb0c7bf324",
	"TopicArn" : "arn:aws:sns:us-east-1:123456789012:MyTopic",
	"Subject" : "My First Message",
	"Message" : "Hello world!",
	"Timestamp" : "2012-05-02T00:54:06.655Z",
	"SignatureVersion" : "1",
	"Signature" : "EXAMPLEw6JRNwm1LFQL4ICB0bnXrdB8ClRMTQFGBqwLpGbM78tJ4etTwC5zU7O3tS6tGpey3ejedNdOJ+1fkIp9F2/LmNVKb5aFlYq+9rk9ZiPph5YlLmWsDcyC5T+Sy9/umic5S0UQc2PEtgdpVBahwNOdMW4JPwk0kAJJztnc=",
	"SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem",
	"UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:MyTopic:c9135db0-26c4-47ec-8998-413945fb5a96"
	}
	"""

	STATUS_PENDING= 'PENDING'
	STATUS_PROCESSED = 'PROCESSED'
	STATUS_ERROR = 'ERROR'
	STATUSES =  (STATUS_PENDING, STATUS_PROCESSED, STATUS_ERROR)

	messageId= models.CharField(max_length=48)
	topicArn = models.CharField(max_length=250)
	subject = models.CharField(max_length=250)
	message = models.TextField()
	timestamp  = models.DateTimeField()
	status = models.CharField(max_length= max(map(len, STATUSES)), choices= zip(STATUSES,map(lambda x: x.capitalize(), STATUSES)), default=STATUS_PENDING) 
	modified = models.DateTimeField(auto_now=True, auto_now_add=True)
	errors =  models.TextField(null=True, blank=True)
	def __unicode__(self):
		return "{}: {} ({}:{})".format(self.topicArn, self.subject,   self.status, self.modified)

	@classmethod
	def add(cls, message):
		notification = Notification.objects.create(
				messageId= message["MessageId"],
				topicArn = message["TopicArn"],
				subject = message["Subject"],
				message = message["Message"],
				timestamp = message["Timestamp"],
		)
		sns_signal.send("ProcessNotificationSender", message=message) 
		return notification
