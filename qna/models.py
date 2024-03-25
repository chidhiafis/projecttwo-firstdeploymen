from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=123)
    body=models.TextField()

    class Meta:
        ordering=['title',]

    def __str__(self):
        return self.title

