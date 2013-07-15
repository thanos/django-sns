from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('sns.views',
    url(r'^endpoint/$', 'sns_endpoint', name='sns_endpoint'),
    url(r'^subscribe/(?P<topic>[^/]+)/$', 'subscribe', name='subscribe'),
)