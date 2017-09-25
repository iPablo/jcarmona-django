from rest_framework import serializers
from . models import Notice, Event
from django.contrib.auth.models import User


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        #fields = ('id', 'name', 'release_date', 'rating', 'category')
        fields = ('title', 'description', 'publish_date')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('title', 'description', 'start_date', 'end_date')

