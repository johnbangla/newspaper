from django.db import models

# Create your models here.

class Bangla(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=4000,null=True,blank=True,default='title')
    papericon = models.ImageField(upload_to='photos', default='default.jpg')
    paperurl = models.CharField(max_length=400,null=True,blank=True,default='myurl')
    

    def __str__(self):
        return self.title
    
    
class English(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=4000,null=True,blank=True,default='title')
    papericon = models.ImageField(upload_to='photos', default='default.jpg')
    paperurl = models.CharField(max_length=400,null=True,blank=True,default='myurl')
    

    def __str__(self):
        return self.title
    
    
    
    
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=4000,null=True,blank=True,default='title')
    videoicon = models.ImageField(upload_to='photos', default='default.jpg')
    videourl = models.CharField(max_length=400,null=True,blank=True,default='myurl')
    

    def __str__(self):
        return self.title       