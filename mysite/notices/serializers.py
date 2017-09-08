from rest_framework import serializers
from . models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        #fields = ('id', 'name', 'release_date', 'rating', 'category')
        fields = ('title', 'description', 'publish_date')


    def create(self, validated_data):
        """Create and return a new `Notice` instance, given the validated data."""
        return Notice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing `Notice` instance, given the validated data."""
        instance.title = validated_data.get('name', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)
        instance.save()
        return instance



