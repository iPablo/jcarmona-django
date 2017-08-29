from django.urls import translate_url
from django.conf.urls import url
from . import views

urlpatterns = [
    #patron pagina de inicio
    url(r'^$', views.index, name='index')
]