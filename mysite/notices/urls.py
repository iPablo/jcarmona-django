from django.urls import translate_url
from django.conf.urls import url

from . import views


urlpatterns = [
    #urls basadas en funciones
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

    #urls basadas en vistas, crear noticia
    url(r'^notices_v2/new/$', views.Notice_new_v2.as_view(), name='notice_new_v2'),

    #url basada en vistas, editar noticia
    url(r'^notices_v2/(?P<pk>[0-9]+)/edit/$', views.Notice_edit_v2.as_view(), name='notice_edit_v2'),

    #url basada en vistas, eliminar noticia
    url(r'^notices_v2/(?P<pk>\d+)/delete/$', views.Notice_delete_v2.as_view(), name='notice_delete_v2'),
]