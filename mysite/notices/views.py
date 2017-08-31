from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.

from . models import Notice, Event
from . forms import PostForm

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

#def notice_detail(request, pk):
#    notice = get_object_or_404(Notice, pk=pk)
#    return render(request, 'notices/notice_detail.html', {'notice': notice})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    context = {'event': event}
    return render(request=request,
                  template_name='notices/event_detail.html',
                  context=context)

def notice_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            #notice.author = request.user
            notice.published_date = timezone.now()
            notice.save()
            return redirect('/', pk=notice.pk)
    else:
        form = PostForm()
    return render(request, 'notices/notice_edit.html', {'form': form})


#def notice_edit(request, pk):
#     notice = Notice.objects.get(pk=pk)
#     if request.method == "POST":
#         context = {'notice': notice}
#         return render(request=request,
#                       template_name='notices/notice_detail.html',
#                       context=context)


def notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            #notice.author = request.user
            notice.save()
            return redirect('notices.views.notice_detail', pk=notice.pk)
    else:
        form = PostForm(instance=notice)
    return render(request, 'notices/notice_edit.html', {'form': form})