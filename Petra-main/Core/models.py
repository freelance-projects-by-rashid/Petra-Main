from django.db import models
from U_Auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

BANNER_TYPES = [('Mobile','Mobile'),('System','System')]

class Banner(models.Model):
    Date = models.DateField(auto_now_add=True)
    Banner_Type = models.CharField(max_length=10,choices=BANNER_TYPES)
    Image = models.ImageField(null=True,upload_to='Banners')

class Gallery_Image(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Gallery')

class Partners(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Partners')

class Schools(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Partners')

class Event(models.Model):
    Added_Date = models.DateField(auto_now_add=True)

    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Description = models.TextField()
    Image = models.ImageField(null=True,upload_to='Events')

    def __str__(self):
        return self.Name
    
class Review(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100,null=True)
    Rating = models.IntegerField(default=0)
    Description = models.TextField()

class Enquiry(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=20,null=True)
    Description = models.TextField()

class Premium(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Premiums')
    Image2 = models.ImageField(null=True,upload_to='Premiums',blank=True)
    Description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Premium.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('testApp:product_detail', args=['premium', self.slug])
    
class Single(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Singles')
    Image2 = models.ImageField(null=True,upload_to='Singless',blank=True)
    Description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Single.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('testApp:product_detail', args=['single', self.slug])
    
class Double(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Doubles')
    Image2 = models.ImageField(null=True,upload_to='Doubles',blank=True)
    Description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Double.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('testApp:product_detail', args=['double', self.slug])
    
