from django.db import models
from django.utils import timezone

class Ticket(models.Model):
    title = models.CharField(max_length=50, blank=False)
    summary = models.CharField(max_length=100, blank=False)
    detail = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True,
    default='static/img/star.png')
    views = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    ticket = models.ForeignKey('pobalStudio.Ticket', on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    comment = models.TextField()
    
    def __str__(self):
        return self.comment