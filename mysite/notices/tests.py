from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Notice, Event
from django.test import Client


#biblia de pasos
#1º Listo las noticias que tengo
#2º get a las noticias (http://miaplicacio/news/create)
#3º Compruebo que el get anterior es un 200
#4º Hago un post a http://miaplicacio/news/create con unos datos.
#5º Compruebo que el post da un 301
#6º Listo de nuevo todas las noticias
#7º Compruebo que las noticias son 1 mas de las que habia en el paso 1º


#test para las urls
class IndexTestCase(TestCase):
    #comprueba que haya noticias ademas de eventos y no este vacio
    def test_notice_exist(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

#test para la funcion Notices
class NoticeTestCase(TestCase):
    #comprueba que haya sido creada una noticia y que exista
    def test_notice_exist(self):
        c = Client()
        noticias = c.post('/notices/new/', {'title': 'test', 'description': 'testtt'})
        if Notice.objects.exists():
            print("existen noticias")
        else:
            print("no existen noticias")

#num_results = User.objects.filter(email=cleaned_info['username']).count()


#test para la funcion Events

#test para la funcion notice_detail

#test para la funcion event_detail

#test para la funcion notice_new
class NoticeNewTestCase(TestCase):
    #una funcion por cada caso, leer, crear, borrar, editar tanto para noticas como eventos
    def test_notice_new(self):
        c = Client()
        notices_before = Notice.objects.order_by('-title').count()
        response = c.get('/notices/new/')
        self.assertEqual(response.status_code, 200)
        response = c.post('/notices/new/', {'title': 'prueba_test', 'description': 'descripcion_test'})
        self.assertEqual(response.status_code, 302)
        notices_after = Notice.objects.order_by('-title').count()
        self.assertEqual(notices_after, notices_before+1)




#test para la funcion notice_edit

#test para la funcion notice_delete
class NoticeDelTestCase(TestCase):
    #una funcion por cada caso, leer, crear, borrar, editar tanto para noticas como eventos
    def test_notice_del(self):
        c = Client()
        notice_created = c.post('/notices/new/', {'title': 'prueba_borrado', 'description': 'descripcion_borrada'})
        notices_before = Notice.objects.order_by('-title').count()
        print(notices_before)



        notices_after = Notice.objects.order_by('-title').count()
        print(notices_after)
        self.assertEqual(notices_before, notices_after-1)
    #no consigo borrar la noticia creada para poder comprobar que se borra