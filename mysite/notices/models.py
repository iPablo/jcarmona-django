from django.db import models
from django.utils import timezone


# Create your models here.

class Base(models.Model):
    title = models.CharField(max_length=30)

    """abstract to false"""
    class Meta:
        abstract = False


class BaseNew(Base):
    #description = models.CharField(max_length=200)
    description = models.TextField()

class Notice(BaseNew):
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Event(BaseNew):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
