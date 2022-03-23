from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
      
    user = models.OneToOneFiled(User, on_delete=models.CASCADE
    
    First_name = models.CharField( max_length=64 )
    last_name = models.CharField ( max_length=64 )
    email = models.CharField ( max_length=64 )
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username    
        
class login(models.Model):
            