from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    content = models.TextField()