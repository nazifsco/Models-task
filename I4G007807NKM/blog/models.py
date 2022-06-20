from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __init__(self):
        return self.title
