from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
'''
django model filds:
==> html widgit
==> validation
==> db size
'''
JOB_TYPE =(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

def image_upload(instence, filename): # helber function to upload image special file
    imagename, extention = filename.split('.')
    return 'jobs/%s.%s' %(instence.id,extention)


# https://docs.djangoproject.com/fr/4.0/ref/models/fields/
class Job(models.Model): # Table
    owner = models.ForeignKey(User, related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #Column
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    discription = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    experience = models.CharField(max_length=50)
    categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)
    
    
    # Oveeride method save
    def save(self,*args, **kwargs):
        #logic
        self.slug = slugify(self.title) # slugify method delete space and add - between title
        super(Job,self).save(*args,**kwargs)
        
        
    def __str__(self):
        return self.title
    
class Categorie(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name