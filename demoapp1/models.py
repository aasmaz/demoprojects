from django.db import models
from django.utils import timezone

# Create your models here.

class LogEntry(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    status_message = models.CharField(max_length=255)


