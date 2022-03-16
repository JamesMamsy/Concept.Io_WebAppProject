from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),

    path('edit_project/<project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='Add Project'),
    path('view_my_project_details/<project_id>/', views.view_project, name='view_project'),
    path('view_projects/', views.view_projects, name='Choose A Project'),
]

