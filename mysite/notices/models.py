from django.db import models
from django.utils import timezone


# Create your models here.

class Base(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        abstract = True

class BaseNew(Base):
    description = models.CharField(max_length=200)

class NewsItem(BaseNew):
    publish_date = models.DateTimeField(default=timezone.now)

class Event(BaseNew):
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ['title']