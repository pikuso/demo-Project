from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title

