from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns(
    'schedule.views',
    url(r'^$', 'index', name="index"),
    url(r'^update/(?P<id>\d+)$', 'update_event', name="update_event"),
    url(r'^myevents/$', 'my_events', name="my_event"),
    url(r'^delete/(?P<id>\d+)$', 'delete_event', name="delete_event"),
    url(r'^month/(?P<month>\d+)/(?P<year>\d+)/(?P<change>[-\w]+)/(?P<param>[-\w]+)$', 'month', name="month"),
    url(r'^create/event/(?P<day>\d+)/(?P<month>[-\w]+)/(?P<year>\d+)$', 'create_event', name="create_event"),
    url(r'^detail/day/(?P<day>\d+)/(?P<month>[-\w]+)/(?P<year>\d+)$', 'detail_day', name="detail_day"),
    url(r'^detail/events/(?P<param>[-\w]+)/$', 'detail_event', name="detail_events"),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
   
)
urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'template_name': 'login.html'}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
   
)