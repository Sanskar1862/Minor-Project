from django.db import models

# Create your models here.
class Image(models.Model):
 photo = models.ImageField(upload_to="media")
#  title = models.CharField(max_length=100)
 date = models.DateTimeField(auto_now_add=True)