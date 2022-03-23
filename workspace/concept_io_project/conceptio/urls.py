from django.urls import path
from conceptio import views

app_name = 'conceptio'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project/<project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='Add Project'),
    path('view_my_projects/', views.view_projects, name='view_my_projects'),
    path('view_project_by_id/<project_id>', views.view_project, name='view_project_by_id'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('like_project/<int:project_id>/', views.LikeView, name='like_project'),
    path('categories/', views.categories, name='categories')
]

