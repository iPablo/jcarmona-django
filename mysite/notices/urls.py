from django.urls import translate_url
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]