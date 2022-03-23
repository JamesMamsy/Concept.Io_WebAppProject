from django.shortcuts import render
<<<<<<< HEAD
=======
from django.shortcuts import render, get_object_or_404



# Create your views here.

>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ImageForm, Project
from django.shortcuts import redirect
<<<<<<< HEAD
from .models import Image,Comment
from django.urls import reverse
from django.models import Page

from .forms import Project,ImageForm
=======
from .models import Category, Image,Comment
from django.urls import reverse

from conceptio.forms import Project,ImageForm
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

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
<<<<<<< HEAD
            p = Project.objects.create(title=title, desc=desc,cat=cat,tags=tags)
=======
            p = Project.objects.create(creator = request.user, title=title, desc=desc,cat=cat,tags=tags)
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
            p.save()
            images = request.FILES.getlist('images')


            for image in images:
                photo = Image.objects.create(image=image, project=p)
                photo.save()
            id=p.project_id
<<<<<<< HEAD
            return redirect(reverse('rango:view_project',kwargs={'project_id':id}))

    return render(request, 'rango/add_project.html',{'form': photo})
=======
            return redirect(reverse('conceptio:view_project',kwargs={'project_id':id}))

    return render(request, 'conceptio/add_project.html',{'form': photo})
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

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
<<<<<<< HEAD


    return render(request, 'rango/edit_project.html',{'form': form})

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'rango/add_project.html')
=======
    else:
        print("nah")
        return redirect(reverse('conceptio:view_project',kwargs={'project_id':id}))



    return render(request, 'conceptio/edit_project.html',{'form': form})

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'conceptio/add_project.html')
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c


def view_project(request,project_id):
    context_dict = {}

    project = Project.objects.get(project_id=project_id)
    comments = Comment.objects.filter(project=project)
    images = Image.objects.filter(project=project)

    context_dict['project'] = project
    context_dict['images'] = images
    context_dict['comments'] = comments


<<<<<<< HEAD
    return render(request, 'rango/view_project_details.html',context_dict)
=======
    return render(request, 'conceptio/view_project_details.html',context_dict)
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

def view_projects(request):
    print(request)

    context_dict = {}
    projects = Project.objects.all()
    context_dict['projects'] = projects

<<<<<<< HEAD



    return render(request, 'rango/view_my_projects.html',context_dict)
=======
    return render(request, 'conceptio/view_my_projects.html',context_dict)
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c



def index(request):

<<<<<<< HEAD
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['pages'] = [page_list]
    return render(request, 'rango/index.html', context = context_dict)
=======
    cat_list = Category.objects.order_by('id')[:5]
    context_dict = {}
    context_dict['cat'] = [cat_list]
    return render(request, 'conceptio/index.html', context = context_dict)
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c



def login(request):
<<<<<<< HEAD
    return render(request, 'login/login.html')
=======
    return render(request, 'conceptio/login.html')

def categories(request):
    
    category_list = {"Category_name_here", "example", "etc."}
    cat_object_list = []
    context_dict = {}
    for cat in category_list:
        tmp_cat = Category.objects.filter(name=cat)
        cat_object_list.append(tmp_cat)
    
    context_dict['categories'] = cat_object_list
    return render(request, 'conceptio/categories.html')

def LikeView(request,project_id):
    project = get_object_or_404(Project, project_id=request.POST.get('project_id'))
    project.likes.add(request.user)
    return redirect(reverse('conceptio:view_project', kwargs={'project_id': request.POST.get('project_id')}))

def view_categories(request):
  context_dict = {}

  categories=Category.objects.all()
  conttext_dict['categories']=categories

  return render(request, 'rango/categories.html',context_dict)


>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

