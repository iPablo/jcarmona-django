from django.urls import translate_url
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notices/$', views.notices, name='notices'),
    url(r'^events/$', views.events, name='events'),

    url(r'^notices/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail, name='event_detail'),

    url(r'^notices/new/$', views.notice_new, name='notice_new'),
    url(r'^notices/(?P<pk>[0-9]+)/edit/$', views.notice_edit, name='notice_edit'),
]