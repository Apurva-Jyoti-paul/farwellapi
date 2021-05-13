from django.db import models
from cloudinary.models import CloudinaryField



class Senior(models.Model):

    name = models.CharField(max_length=100)
    dp = CloudinaryField('image')

    def __str__(self):
        return self.name

class Seniorinfo(models.Model):

    senior= models.ForeignKey(Senior,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    description2 =models.CharField(max_length=1000,null=True)
    sname = models.CharField(max_length=100,null=True)
    pic = CloudinaryField('pic',null=True)
    
    def __str__(self):
        return self.sname

class awards(models.Model):

    info= models.ForeignKey(Seniorinfo,related_name='award',on_delete=models.CASCADE)
    myaward = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.myaward
    


class imagegallery(models.Model):

    desc= models.ForeignKey(Seniorinfo,related_name='gall',on_delete=models.CASCADE)
    im = CloudinaryField('imgallery')

class ratings(models.Model):
    
    senior=models.ForeignKey(Seniorinfo,related_name='rat',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    rate=models.IntegerField(default=10)

    def __str__(self):
        return self.name


   
# Create your models here.
