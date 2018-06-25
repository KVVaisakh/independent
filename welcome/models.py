from django.db import models
from django.utils import timezone
# Create your models here.
class Url(models.Model):
    url=models.CharField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True,auto_now=False)
    update=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.url
