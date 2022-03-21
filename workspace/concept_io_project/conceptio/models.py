from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify




class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project_id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=120)
    desc = models.CharField('Description',max_length=300)
    cat = models.CharField('Category', max_length=300,default='')
    tags = models.CharField('Tags', max_length=300,default='')
    likes = models.ManyToManyField(User,related_name = "project_likes")
    dislikes = models.IntegerField('dislikes', default=0)
    slug = models.SlugField(unique=True)


    def total_likes(self):
        return self.likes.count()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):

    project = models.ForeignKey(Project,on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to = 'media',null=True, blank=True)
    def __str__(self):
        return self.image


class Comment(models.Model):
    # commentor - User that created comment, foreign key
    project = models.ForeignKey(Project,related_name="comments",on_delete=models.SET_NULL, null=True, blank=True)
    commentor = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField('Comment', max_length=3000)

    def __str__(self):
        return self.comment

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=100)

    def __str__(self):
        return self.name