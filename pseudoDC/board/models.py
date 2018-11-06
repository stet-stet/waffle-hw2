from django.db import models
from django.utils import timezone

# Create your models here.


class BlogPost(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    password = models.CharField(max_length=200, default="1111")
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
