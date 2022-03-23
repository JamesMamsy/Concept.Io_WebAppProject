from django.shortcuts import render

from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ImageForm, Project
from django.shortcuts import redirect
from .models import Image,Comment, Page
from django.urls import reverse
# from django.models import Page

from .forms import Project,ImageForm

from django.views.generic.edit import FormView



def add_project(request):
    photo = ImageForm()
    form = ImageForm(request.POST or None, request.FILES or None)
    files = request.FILES.getlist('images')
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            cat = form.cleaned_data['cat']
            tags = form.cleaned_data['tags']
            p = Project.objects.create(title=title, desc=desc,cat=cat,tags=tags)
            p.save()
            images = request.FILES.getlist('images')


            for image in images:
                photo = Image.objects.create(image=image, project=p)
                photo.save()
            id=p.project_id
            return redirect(reverse('rango:view_project',kwargs={'project_id':id}))

    return render(request, 'rango/add_project.html',{'form': photo})

def edit_project(request,project_id):
    # This only currently loads all fields except images and updates all fields except images
    project=Project.objects.get(project_id=project_id)
    images = Image.objects.filter(project=project)

    form = ImageForm(request.POST or None, instance = project)



    if form.is_valid():
        form.save()
        images = request.FILES.getlist('images')
        for image in images:
            photo = Image.objects.get(project=p)
            photo.save()


    return render(request, 'rango/edit_project.html',{'form': form})

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'rango/add_project.html')


def view_project(request,project_id):
    context_dict = {}

    project = Project.objects.get(project_id=project_id)
    comments = Comment.objects.filter(project=project)
    images = Image.objects.filter(project=project)

    context_dict['project'] = project
    context_dict['images'] = images
    context_dict['comments'] = comments


    return render(request, 'rango/view_project_details.html',context_dict)

def view_projects(request):
    print(request)

    context_dict = {}
    projects = Project.objects.all()
    context_dict['projects'] = projects




    return render(request, 'rango/view_my_projects.html',context_dict)



def index(request):

    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['pages'] = [page_list]
    return render(request, 'rango/index.html', context = context_dict)


