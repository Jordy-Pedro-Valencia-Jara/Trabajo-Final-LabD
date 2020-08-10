from django.db import models

# Create your models here.
class chef(models.Model):
    name=models.CharField(max_length=100)
    las_name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    email=models.EmailField()
class platillo(models.Model): 
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    Brev=models.CharField(max_length=100)
    price=models.IntegerField()
    chef_cocinero=models.ForeignKey(chef,on_delete=models.CASCADE,blank=False,null=True)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()



