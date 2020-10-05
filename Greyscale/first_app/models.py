from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=264)
    last_name=models.CharField(max_length=264)
    email=models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return self.name
