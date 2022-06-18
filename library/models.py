from django.db import models
from django.urls import reverse

# Create your models here.

class categories(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class books(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    categ = models.ForeignKey(categories,on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='Book_cover',default='Book_cover/default.jpg')
    def get_url(self):
        return reverse('details',args=[self.categ.slug,self.slug])
