from django.db import models

# Create your models here.
class Path(models.Model):
    tag=models.CharField(max_length=150)
    paragraph=models.CharField(max_length=500)
    date=models.DateTimeField()
