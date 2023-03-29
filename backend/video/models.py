from django.db import models
# Create your models here.

class Video(models.Model):
    video_title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_add_now=True)
    video = models.FileField(upload_to='videos/', null=True)
    rated = models.IntegerField(default=0)
