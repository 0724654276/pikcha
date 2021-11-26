from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location =  models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    
  def __str__(self):
        return self.name