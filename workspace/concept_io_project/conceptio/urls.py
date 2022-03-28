from django.urls import path
from conceptio import views

app_name = 'conceptio'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project/<project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='Add Project'),
    path('view_my_project_details/<project_id>/', views.view_project, name='view_project'),
    path('view_projects/', views.view_projects, name='Choose A Project'),
    path('login/', views.login, name='login'),
    path('like_project/<int:project_id>/', views.LikeView, name='like_project'),
    path('categories/', views.categories, name='categories')
]

