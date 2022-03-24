from django.urls import path
from conceptio import views

app_name = 'conceptio'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_project/<project_id>/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='Add Project'),
    path('view_my_project_details/<project_id>/', views.view_project, name='view_project'),
    path('view_my_projects/', views.view_projects, name='view_my_projects'),
    path('like_project/<int:project_id>/', views.LikeView, name='like_project'),

    path('categories/', views.categories, name='categories'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('view_projects_by_tag/<search_criteria>/', views.view_projects_by_tag, name='view_projects_by_tag'),
    path('view_projects_by_category/<category>/', views.view_projects_by_category, name='view_projects_by_category'),
    path('search/', views.search, name='search'),
]

