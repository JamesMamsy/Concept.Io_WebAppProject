from django.shortcuts import render
from django.models import Page
from rango.forms import UserForm, UserProfileForm

def index(request):
    page_list = Page.objects.order_by('-views')[0:10]
    design_day = Page.objects.order_by('-likes')[:1]
    new_pages = Page.objects.order_by('-id')[0:10]
    
    context_dict = {}
    context_dict['dotd'] = [design_day]
    context_dict['pages'] = [page_list]
    context_dict['additions'] = [new_pages]
    
    return render(request, 'rango/index.html', context = context_dict)

def login(request):
    return render(request, 'rango/login.html') 

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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Concept.io account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")

    else: 
        return render(request, 'Concept_io/login.html', {})