from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse

from .models import Notice, Event

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
        #cuenta cuantas noticias hay, no debe de haber ninguna
        notices_before = Notice.objects.order_by('-title').count()
        #comprueba que existe y funciona la url notice_new, con reverse la rescata de urls.py
        response = c.get(reverse('notice_new'))
        self.assertEqual(response.status_code, 200)
        #crea una noticia con titulo y descripcion
        response = c.post(reverse('notice_new'), {'title': 'prueba_test', 'description': 'descripcion_test'})
        #comprueba que haya una redirección al crear la noticia
        self.assertEqual(response.status_code, 302)
        #vuelve a contar cuantas noticias hay
        notices_after = Notice.objects.order_by('-title').count()
        #compara que tiene que haber una noticia mas
        self.assertEqual(notices_after, notices_before+1)




#test para la funcion notice_edit
#es parecido a noticenewtestcase y noticedeltestcase
#tengo que crear una noticia, capturar los datos y modificarla, despues comparar que titulo, descripcion no sean iguales
class NoticeEditTestCase(TestCase):
    def test_notice_edit(self):
        c = Client()
        #creo una noticia
        c.post(reverse('notice_new'), {'title': 'primera_noticia', 'description': 'primera_descripcion'})

        import ipdb;
        ipdb.set_trace()

        #identifico el titulo y lo guardo
        titulo = Notice.objects.get(title='prueba_borrado')



        #edito el titlo que obtuve
        c.post(reverse('notice_edit',{'title': 'primera_noticia', 'description': 'primera_descripcion'}, kwargs={'pk': titulo.pk}))


        #c.post(reverse('notice_edit'), {'title': 'primera_noticia_modificada', 'description': 'primera_descripcion'})
        #titulo_modificado = Notice.objects.filter(obtener pk de la anterior noticia modificada)



        #comparar los titulos, si la noticia ha sido modificada, OK
        self.assertEqual(titulo, titulo_modificado)

#test para la funcion notice_delete
class NoticeDelTestCase(TestCase):
    # elimina la noticia creada realiza una comprobacion
    def test_notice_del(self):
        c = Client()
        #crea una noticia con titulo y descripcion
        c.post(reverse('notice_new'), {'title': 'prueba_borrado', 'description': 'descripcion_borrada'})
        #guarda el numero de noticias
        notices_before = Notice.objects.all().count()
        print(notices_before)
        #borra la noticia creada
        notice = Notice.objects.get(title='prueba_borrado')
        c.delete(reverse('notice_delete', kwargs={'pk': notice.pk}))
        #vuelve a contar cuantas noticias hay
        notices_after = Notice.objects.all().count()
        print(notices_after)
        #compara que sea distinto las noticias, tiene que haber una menos
        self.assertNotEqual(notices_before, notices_after)
