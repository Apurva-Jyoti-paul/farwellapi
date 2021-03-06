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
    pict = CloudinaryField('pict',null=True)
    
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

class fav_place(models.Model):

    senior = models.ForeignKey(Seniorinfo,related_name='favplace',on_delete=models.CASCADE)
    imag = CloudinaryField('imag')
    description = models.CharField(max_length=1000,null=True)
    place = models.CharField(max_length=20,null=True)

# Create your models here.


class messages(models.Model):

    senior= models.ForeignKey(Seniorinfo,related_name='message',on_delete=models.CASCADE)
    comment= models.CharField(max_length=1000,null=True)
    author = models.CharField(max_length=15,null=True)