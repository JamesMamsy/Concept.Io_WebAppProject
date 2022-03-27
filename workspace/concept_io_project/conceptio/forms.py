from django import forms
from django.forms import ModelForm,TextInput,EmailInput
from conceptio.models import Project,Image, Category, Comment
class ProjectForm(ModelForm):

    class Meta:
        model = Project


        # CHOICES will be replaced by categories stored in db
        
        CHOICES = tuple(Category.objects.values_list('id', 'name'))


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

class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['comment',]

