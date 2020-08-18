 
from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100,blank=True)
    info = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True,blank=True)
    name = models.CharField(max_length=20,default='name')
    email = models.EmailField(max_length=100,default='email')
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    bio = models.TextField(max_length=100,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )

    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    usability_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    design_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    content_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()