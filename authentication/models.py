from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Tag(models.Model):
    language= models.CharField(max_length=50)
    stage= models.CharField(max_length=80)
    logical=models.BooleanField(default=True)
    technical=models.BooleanField(default=False)
