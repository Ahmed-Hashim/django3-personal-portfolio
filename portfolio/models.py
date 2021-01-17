from django.db import models
from django.db.models.fields import URLField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    #show name in admin
    def __str__(self):
        return self.title
class Port(models.Model):
    title = models.CharField(max_length=100,default=None)
    home_image = models.ImageField(upload_to='portfolio/images/')
    home_logo = models.ImageField(upload_to='portfolio/images/')
    des = models.CharField(max_length=250,default=None)

