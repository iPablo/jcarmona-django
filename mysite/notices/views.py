from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

from . models import Notice

def index(request):
    #return HttpResponse("Hello, your are in the index notices")
     latest_notice_list = Notice.objects.order_by('-publish_date')[:5]
     context = {'latest_notice_list': latest_}
     return HttpResponse(output)


# class IndexView(generic.ListView):
#    template_name = 'notices/index.html'
#    context_object_name = 'latest_notices_list'

    #def get_queryset(self):
    #    return Notices.ob