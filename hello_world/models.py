from django.db import models
#In Django, the MEDIA_ROOT setting is where we define the location of all user uploaded items2
# Create your models here.
class Project(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='img/')#The location of the uploaded image will be in MEDIA_ROOT/images
    # image = models.FilePathField(path='/img')
    def __str__(self):
        return self.title

