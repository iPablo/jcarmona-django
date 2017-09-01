from django.urls import translate_url
from django.conf.urls import url

from . import views


urlpatterns = [

    #default page index
    url(r'^$', views.index, name='index'),

    #url list notices only
    url(r'^notices/$', views.notices, name='notices'),

    #url list events only
    url(r'^events/$', views.events, name='events'),

    #url shows details notice
    url(r'^notices/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),

    #url shows details events
    url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail, name='event_detail'),

    #url when create your notice
    url(r'^notices/new/$', views.notice_new, name='notice_new'),

    #url when edit your notice
    url(r'^notices/(?P<pk>[0-9]+)/edit/$', views.notice_edit, name='notice_edit'),

    #url when delete your notice
    url(r'^notices/(?P<pk>\d+)/delete/$', views.notice_delete, name='notice_delete'),

]