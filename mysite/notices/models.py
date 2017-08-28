from django.db import models
from django.utils import timezone

# Create your models here.
#clase
class notice (models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)