from django.urls import path
from conceptio import views
from registration.backends.simple.views import RegistrationView
from django.urls import reverse


app_name = 'conceptio'

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('conceptio:register_profile')


urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project/<project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='Add Project'),
    path('view_my_project_details/<project_id>/', views.view_project, name='view_project'),
    path('view_projects/', views.view_projects, name='Choose A Project'),
    path('login/', views.login, name='login'),
    path('Register_here/', views.Register_here, name=' Register Here'),
    path('Register/', views.Register, name = 'Register'),
    
]

