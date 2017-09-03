from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.utils import timezone

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

from . models import Notice, Event
from . forms import PostForm

def index(request):
    """Order notices by title and render on /notices/"""
    latest_notice_list = Notice.objects.order_by('-title')
    latest_event_list = Event.objects.order_by('-title')
    context = {'latest_notice_list': latest_notice_list,
               'latest_event_list': latest_event_list,
               }
    return render(request, 'notices/index.html', context)

def notices(request):
    """Order only notices by title"""
    latest_notice_list = Notice.objects.order_by('-title')
    context = {'latest_notice_list': latest_notice_list,}

    return render(request, 'notices/notices.html', context)

def events(request):
    """Order only events by title"""
    latest_event_list = Event.objects.order_by('-title')
    context = {'latest_event_list': latest_event_list,}

    return render(request, 'notices/events.html', context)


def notice_detail(request, pk):
    """get key and show details of a notice"""
    notice = Notice.objects.get(pk=pk)
    context = {'notice': notice}
    return render(request=request,
                  template_name='notices/notice_detail.html',
                  context=context)

def event_detail(request, pk):
    """get key and show details of a event"""
    event = Event.objects.get(pk=pk)
    context = {'event': event}
    return render(request=request,
                  template_name='notices/event_detail.html',
                  context=context)

def notice_new(request):
    """post with current date the new notice"""
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


def notice_edit(request, pk):
    """edit the notice"""
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            #notice.author = request.user
            notice.save()
            return redirect('/', pk=notice.pk)
    else:
        form = PostForm(instance=notice)
    return render(request, 'notices/notice_edit.html', {'form': form})


def notice_delete(request, pk):
    """delete the notice"""
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('/', pk=notice.pk)

# visto con surber
class Notice_new_v2(CreateView):
    """notice created based view"""
    model = Notice
    fields = ['title', 'description']
    #form_class = PostForm2
    template_name = 'notices/new_notice_v2.html'

    #def get_success_url(self):
    #    return reverse('notice_detail', args=(self.object.id,))

    def get_success_url(self):
        return reverse(index)

class Notice_edit_v2(UpdateView):
    """notice edit based view"""
    model = Notice
    fields = ['title', 'description']
    template_name = 'notices/notice_edit_v2.html'

    def get_success_url(self):
        return reverse('notice_detail', args=(self.object.id,))


class Notice_delete_v2(DeleteView):
    """notice delete based view"""
    model = Notice
    #fields = ['title', 'description']
    success_url = reverse_lazy(index)


