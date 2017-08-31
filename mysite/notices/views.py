from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

from . models import Notice, Event

"""Order notices by title and render on /notices/"""
def index(request):
    latest_notice_list = Notice.objects.order_by('-title')
    latest_event_list = Event.objects.order_by('-title')
    context = {'latest_notice_list': latest_notice_list,
               'latest_event_list': latest_event_list,
               }
    return render(request, 'notices/index.html', context)

def notices(request):
    latest_notice_list = Notice.objects.order_by('-title')
    context = {'latest_notice_list': latest_notice_list,}

    return render(request, 'notices/notices.html', context)

def events(request):
    latest_event_list = Event.objects.order_by('-title')
    context = {'latest_event_list': latest_event_list,}

    return render(request, 'notices/events.html', context)


def notice_detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    context = {'notice': notice}
    return render(request=request,
                  template_name='notices/notice_detail.html',
                  context=context)

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    context = {'event': event}
    return render(request=request,
                  template_name='notices/event_detail.html',
                  context=context)


