from django.db import models
from django.conf import settings
from django.utils import timezone

class Ticket(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=50, blank=False)
    summary = models.CharField(max_length=100, blank=False)
    detail = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True,
    default="img/pobal_sphere.png")
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='ticket_likes')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    ticket = models.ForeignKey('pobalStudio.Ticket', on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    comment = models.TextField()
    
    def __str__(self):
        return self.comment