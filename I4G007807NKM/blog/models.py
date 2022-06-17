from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __init__(self):
        return self.title
