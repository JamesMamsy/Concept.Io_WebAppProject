from django.urls import path
<<<<<<< HEAD
from rango import views

app_name = 'rango'
=======
from conceptio import views

app_name = 'conceptio'
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project/<project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='Add Project'),
    path('view_my_project_details/<project_id>/', views.view_project, name='view_project'),
    path('view_projects/', views.view_projects, name='Choose A Project'),
    path('login/', views.login, name='login'),
<<<<<<< HEAD
=======
    path('categories/', views.categories, name='categories')
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
]

