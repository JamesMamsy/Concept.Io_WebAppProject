from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ImageForm, Project
from django.shortcuts import redirect
from .models import Category, Image,Comment, UserProfile
from django.urls import reverse
from django.contrib.auth.models import User


from conceptio.forms import Project,ImageForm, CommentForm, SearchForm
from conceptio.forms import UserForm, UserProfileForm
from django.views.generic.edit import FormView
from django.views import View
from django.template.defaulttags import register as func_register




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
            return redirect(reverse('conceptio:view_project_by_id',kwargs={'project_id':id}))

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
        return redirect(reverse('conceptio:view_project_by_id',kwargs={'project_id':id}))

    else:
        print("nah")
        return render(request, 'conceptio/edit_project.html',{'form': form})


    

def about(request):
    # Spoiler: you don't need to pass a context dictionary here.
    return render(request, 'conceptio/add_project.html')


def view_project_by_id(request,project_id):
    context_dict = {}

    project = Project.objects.get(project_id=project_id)
    comments = Comment.objects.filter(project=project).order_by('-id')
    images = Image.objects.filter(project=project)
    total_likes = get_object_or_404(Project,project_id=project_id).total_likes
    print((comments))
    context_dict['project'] = project
    context_dict['images'] = images
    context_dict['comments'] = comments
    context_dict['likes'] = total_likes

    category = Category.objects.get(name = project.cat)
    context_dict['category'] = category.name


    form = CommentForm(request.POST or None)
    context_dict['form'] = form
    print (form)
    if request.method == "POST":
        if form.is_valid():
            comment = form.cleaned_data['comment']

            p = Comment.objects.create(project=project, commentor = request.user, comment = comment)
            p.save()
            return redirect(reverse('conceptio:view_project_by_id',kwargs={'project_id':project_id}))

    return render(request, 'conceptio/view_project_details.html',context_dict)

#Should be view_my_projects, leaving in for lack of refactoring ability
def view_projects(request):

    context_dict = {}
    user = request.user
    
    projects = Project.objects.filter(creator=user)
    context_dict['projects'] = projects
    context_dict['project_images'] = {}
    for project in projects:
        images = Image.objects.filter(project=project)
        context_dict['project_images'][project]=images

    return render(request, 'conceptio/view_my_projects.html',context_dict)



def index(request):

    popular_projects = Project.objects.order_by('likes')
    if popular_projects:
        popular_projects = Project.objects.order_by('likes').reverse()[:5]
    
    
    if Project.objects.count() > 5:
        featured_choices = Project.objects.order_by('project_id').reverse()[5:]
        featured = Project.objects.order_by('project_id').reverse()[0]

        for projects in featured_choices:
            if projects.total_likes() > featured.total_likes():
                featured = projects
    else:
        featured = Project.objects.first()
         

    if Project.objects.count() > 10:
        new_projects = Project.objects.order_by('project_id').reverse()[10:]
    else:
        new_projects = Project.objects.order_by('project_id').reverse()

    context_dict = {}
    context_dict['new'] = new_projects
    context_dict['popular_projects'] = popular_projects
    context_dict['featured'] = [featured]
    context_dict['popular_project_images'] = {}
    context_dict['featured_project_images'] = {}
    context_dict['new_project_images'] = {}
    for project in [featured]:
        images = Image.objects.filter(project=project)
        context_dict['featured_project_images'][project]=images
    for project in new_projects:
        images = Image.objects.filter(project=project)
        context_dict['new_project_images'][project]=images
    for project in popular_projects:
        images = Image.objects.filter(project=project)
        context_dict['popular_project_images'][project]=images
    return render(request, 'conceptio/index.html', context = context_dict)

def categories(request):
    context_dict={}
    category_list=Category.objects.all()
    
    context_dict['categories'] = category_list
    return render(request, 'conceptio/categories.html',context_dict)

def LikeView(request,project_id):
    project = get_object_or_404(Project, project_id=request.POST.get('project_id'))
    project.likes.add(request.user)
    return redirect(reverse('conceptio:view_project_by_id', kwargs={'project_id': request.POST.get('project_id')}))

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

    return render(request, 'conceptio/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_logout(request):
    logout(request)
    return redirect(reverse('conceptio:index'))

def search(request):
    search = SearchForm(request.POST or None)

    if request.method == "POST":
        if search.is_valid():
            print("alrighht")
            criteria = search.cleaned_data['search']
            print(criteria)

            return redirect(reverse('conceptio:view_projects_by_tag', kwargs={'search_criteria': criteria}))

    return render(request, 'conceptio/search.html',{'form': search})

def view_projects_by_tag(request,search_criteria):
    show=False
    projects_to_be_showed=[]
    projects=Project.objects.all()
    for project in projects:
        for tag in search_criteria.split():
            if tag in project.tags.split():
                show=True
            else:
                show=False
        if show:
            projects_to_be_showed.append(project)


        context_dict={'projects':projects_to_be_showed}


    return render(request, 'conceptio/view_projects_by_tag.html',context_dict)

def view_projects_by_category(request,category):
    print(category)
    x=Category.objects.get(name=category)
    name=x.name
    projects=Project.objects.filter(cat=x.id)
    print(projects)
    context_dict = {'projects': projects}
    context_dict['cat']= name

    return render(request, 'conceptio/view_projects_by_category.html', context_dict)

def ProfileView(View):
    
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'website': user_profile.website,
                                'picture': user_profile.pictures})

        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('conceptio:index'))

        context_dict = {'user_profile': user_profile, 'selected_user': user, 'form': form}

        return render(request, 'conceptio/profile.html', context_dict)
        
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('conceptio:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect('conceptio/profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile, 'selected_user': user, 'form':form}
       
        return render(request, 'conceptio/profile.html', context_dict)       

@func_register.filter
def get_item(dictionary, key):
    return dictionary.get(key)