from django import forms
from django.forms import ModelForm,TextInput,EmailInput
<<<<<<< HEAD
from .models import Project,Image
from .models import Image
=======
from conceptio.models import Project,Image, Category, Comment
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
class ProjectForm(ModelForm):

    class Meta:
        model = Project


        # CHOICES will be replaced by categories stored in db
<<<<<<< HEAD
        CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)

=======
        
        CHOICES = tuple(Category.objects.values_list('id', 'name'))
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c


        fields = ['title', 'desc', 'cat','tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 700px;'
            }),
            'desc': forms.Textarea(attrs={

                'class': "form-control",
                'style': 'max-width: 700px;'
            }),
            'cat': forms.Select(attrs={

                'class': "form-control",
                'style': 'max-width: 700px;'
            },choices=CHOICES),
            'tags': forms.TextInput(attrs={

                'class': "form-control",
                'style': 'max-width: 700px;'
            })

        }

class ImageForm(ProjectForm):
    images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True,'class': "form-control",'style': 'max-width: 700px;'}),required=False)

    class Meta(ProjectForm.Meta):

        fields = [ProjectForm.Meta.fields[0]] + [ProjectForm.Meta.fields[1]]+['images',]+[ProjectForm.Meta.fields[2]]+[ProjectForm.Meta.fields[3]]
<<<<<<< HEAD
=======

class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['comment',]

>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
