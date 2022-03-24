from django import forms
from django.forms import ModelForm,TextInput,EmailInput
from conceptio.models import Project,Image,Category,Comment,User
from conceptio.models import Image



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

        def __init__(self, *args, **kwargs):
            super(My_Form, self).__init__(*args, **kwargs)
            self.fields['cat'].required = False

class ImageForm(ProjectForm):
    images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True,'class': "form-control",'style': 'max-width: 700px;'}),required=False)

    class Meta(ProjectForm.Meta):

        fields = [ProjectForm.Meta.fields[0]] + [ProjectForm.Meta.fields[1]]+['images',]+[ProjectForm.Meta.fields[2]]+[ProjectForm.Meta.fields[3]]

class CommentForm(ModelForm):

    class Meta:
        model = Comment



        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 700px;'
            })}

class SearchForm(forms.Form):
    search = forms.CharField(max_length=200)


class UserForm(ModelForm):



    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 700px;'
            }),


            'password': forms.PasswordInput(attrs={

                'class': "form-control",
                'style': 'max-width: 700px;'
            })}





class UserProfileForm(ModelForm):
    image = forms.FileField(
        widget=forms.FileInput(attrs={'multiple': True, 'class': "form-control", 'style': 'max-width: 700px;'}),
        required=False)
    class Meta:
        model = User
        fields = ('email','website','image',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 700px;'
            }),

            'website': forms.TextInput(attrs={

                'class': "form-control",
                'style': 'max-width: 700px;'
            })}

