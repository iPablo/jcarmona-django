from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

from . models import Notice, Event

def index(request):
    #return HttpResponse("Hello, your are in the index notices")
    """Order notices by title and render on /notices/"""
    latest_notice_list = Notice.objects.order_by('-title')
    latest_event_list = Event.objects.order_by('-title')
    context = {'latest_notice_list': latest_notice_list,
               'latest_event_list': latest_event_list,
               }
    return render(request, 'notices/index.html', context)
    #return render(request, 'events/index.html', context)


# class IndexView(generic.ListView):
#    template_name = 'notices/index.html'
#    context_object_name = 'latest_notices_list'

    #def get_queryset(self):
    #    return Notices.ob