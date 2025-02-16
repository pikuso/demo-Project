from django.utils import timezone
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    date_published = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return self.title
