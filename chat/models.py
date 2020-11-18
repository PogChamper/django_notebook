from django.db import models

# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author
