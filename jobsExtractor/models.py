from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="")
    source = models.CharField(max_length=200, default="")

    url = models.URLField(max_length=2000, verbose_name="URL")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.company

