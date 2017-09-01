from django.db import models
from django.utils import timezone

# Create your models here.
class Base(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        abstract = False


class BaseNew(Base):
    description = models.TextField()


class Notice(BaseNew):
    """Notice gets description from BaseNew and title getting from base"""
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Event(BaseNew):
    """events obtain description and title getting from BaseNew and Base"""
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
