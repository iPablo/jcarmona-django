from django.urls import translate_url
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notices/$', views.notices, name='notices'),
    url(r'^events/$', views.events, name='events'),
]