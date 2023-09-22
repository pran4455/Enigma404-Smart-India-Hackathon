from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)


class AudioRecording(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_recordings/')
    created_at = models.DateTimeField(auto_now_add=True)