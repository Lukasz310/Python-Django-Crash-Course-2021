from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    slug = models.SlugField(max_length=255)