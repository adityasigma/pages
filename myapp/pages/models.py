from django.db import models
from django.contrib.auth.models import User

class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    request_type = models.CharField(max_length=50)
    request_body = models.CharField(max_length=500)
    request_time = models.DateTimeField()
    response = models.CharField(max_length=500)
    response_time = models.DateTimeField()




# Create your models here.
