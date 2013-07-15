#! -*- coding: utf-8 -*-
"""
    sns.management.commands.route_tweets
    ~~~~~~~~~~~~~~~~~~~

    Collects from Gnip and dumps on rabbitmq

    :copyright: (c) 2013 by thanos vassilakis

    All rights reserved.
"""

__author__ = 'thanos'
__version__='1.0'


import boto, pprint, logging, time

logger = logging.getLogger(__name__)
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings


from sns.models import Subscription







class Command(BaseCommand):
    args = ''
    help = '''Scans the rabbit queues'''


    option_list = BaseCommand.option_list + (
        make_option('--verbose', action='store_true', default=False, help='be verbose, default: %s' % False),
        make_option('--debug', action='store_true', default=False, help='enable debug logging, default: %s' % False),
        make_option( '--dryrun', action='store_true', default=False, help='dry run process - no tweets will be saved: %s' % False),   
        make_option( '--running', action='store_true', default=False, help='dry run process - no tweets will be saved: %s' % False),      
    )



    
    def handle(self, *args, **options):
        print '-'*20, time.ctime(), '-'*20
        print
        print self.handle, args, options
        print 'starting'
        if args[0] == 'subscribe':
            Subscription.subscribe(args[1])
            for sub in Subscription.objects.all():
                print sub
        elif args[0] == 'subs':
            if args[1] == 'list':
                for sub in Subscription.objects.all():
                    print sub