from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ImageForm, Project
from django.shortcuts import redirect
from .models import Category, Image,Comment
from django.urls import reverse

from conceptio.forms import Project,ImageForm, CommentForm
from conceptio.forms import UserForm, UserProfileForm
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
            p = Project.objects.create(creator = request.user, title=title, desc=desc,cat=cat,tags=tags)
            p.save()
            images = request.FILES.getlist('images')


            for image in images:
                photo = Image.objects.create(image=image, project=p)
                photo.save()
            id=p.project_id
            return redirect(reverse('conceptio:view_project',kwargs={'project_id':id}))

    return render(request, 'conceptio/add_project.html',{'form': photo})

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
        return redirect(reverse('conceptio:view_project',kwargs={'project_id':id}))

    else:
        print("nah")
        return render(request, 'conceptio/edit_project.html',{'form': form})


    

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'conceptio/add_project.html')


def view_project(request,project_id):
    context_dict = {}

    project = Project.objects.get(project_id=project_id)
    comments = Comment.objects.filter(project=project)
    images = Image.objects.filter(project=project)
    total_likes = get_object_or_404(Project,project_id=project_id).total_likes

    context_dict['project'] = project
    context_dict['images'] = images
    context_dict['comments'] = comments
    context_dict['likes'] = total_likes

    form = CommentForm(request.POST or None)
    print (form)
    if request.method == "POST":
        if form.is_valid():
            comment = form.cleaned_data['comment']

            p = Comment.objects.create(project=project, commentor = request.user, comment = comment)
            p.save()


    context_dict['form'] = form
    return render(request, 'conceptio/view_project_details.html',context_dict)

#Should be view_my_projects, leaving in for lack of refactoring ability
def view_projects(request):
    print(request)

    context_dict = {}
    user = request.user
    projects = Project.objects.filter(creator=user)
    context_dict['projects'] = projects

    return render(request, 'conceptio/view_my_projects.html',context_dict)



def index(request):

    popular_projects = Project.objects.order_by('likes')[:5]

    featured_choices = Project.objects.order_by('id')[-5:]
    featured = Project.objects.order_by('id')[-1:]
    for projects in featured_choices:
        if projects.total_likes() > featured.total_likes():
            featured = projects

    new_projects = Project.objects.order_by('id')[-10:]


    featured = Project.objects.order_by('')
    context_dict = {}
    context_dict['popular_projects'] = [popular_projects]
    context_dict['featured'] = [featured]
    context_dict['new'] = new_projects

    return render(request, 'conceptio/index.html', context = context_dict)

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
  context_dict['categories']=categories

  return render(request, 'rango/categories.html',context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return redirect(reverse('conceptio:index'))
            else:
                return HttpResponse("Your Concept.io account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")

    else: 
        return render(request, 'conceptio/login.html', {})

def register(request): 

    registered = False
    
    if request.method == 'POST':
    
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
        
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            registered = True
            
        else:

            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_logout(request):
    logout(request)
    return redirect(reverse('conceptio:index'))