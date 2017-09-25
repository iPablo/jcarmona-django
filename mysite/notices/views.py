from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from . serializers import NoticeSerializer, EventSerializer
from . permissions import IsOwnerOrReadOnly


from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator




# Create your views here.

from . models import Notice, Event
from . forms import PostForm, PostForm_event

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

@login_required
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

@login_required
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

@login_required
def notice_delete(request, pk):
    """delete the notice"""
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('/', pk=notice.pk)

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


class Event_new_v2(CreateView):
    """events created based view"""
    #model = Event
    #fields = ['title', 'description', 'start_date', 'end_date']
    form_class = PostForm_event

    template_name = 'notices/new_event_v2.html'

    def get_success_url(self):
        return reverse(index)


class Event_edit_v2(UpdateView):
    """event edit based view"""
    form_class = PostForm_event
    #model = Event
    #fields = ['title', 'description', 'start_date', 'end_date']
    template_name = 'notices/event_edit_v2.html'
    def get_queryset(self):
        return Event.objects.all()

    def get_success_url(self):
        return reverse('event_detail', args=(self.object.id,))

class Event_delete_v2(DeleteView):
    """Event delete based view"""
    form_class = PostForm_event
    success_url = reverse_lazy(index)

    def get_queryset(self):
        return Event.objects.all()




# class JSONResponse(HttpResponse):
#     """An HttpResponse that renders its content into JSON."""
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def notice_list_api(request):
#     """ List all code notice, or create a new notice."""
#     if request.method == 'GET':
#         notice = Notice.objects.all()
#         serializer = NoticeSerializer(notice, many=True)
#         return JSONResponse(serializer.data)
#
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = NoticeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def notice_detail_api(request, pk):
#     """Retrieve, update or delete a notice."""
#     try:
#         notice = Notice.objects.get(pk=pk)
#     except Notice.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = NoticeSerializer(notice)
#         return JSONResponse(serializer.data)
#     # return render(request, 'notices/notices_api.html', context)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = NoticeSerializer(notice, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         notice.delete()
#         return HttpResponse(status=204)


class EventListAPI(generics.ListCreateAPIView):
    """Class EventListAPI"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

