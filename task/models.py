from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='L',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail',kwargs={'pk':self.pk})
