from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    data = models.TextField()
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(auto_now=True)
