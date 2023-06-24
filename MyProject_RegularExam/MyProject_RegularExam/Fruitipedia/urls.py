from django.urls import path
from MyProject_RegularExam.Fruitipedia import views

app_name = 'fruitipedia'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create_fruit'),
    path('<int:fruit_id>/details/', views.fruit_details, name='fruit_details'),
    path('<int:fruit_id>/edit/', views.edit_fruit, name='edit_fruit'),
    path('<int:fruit_id>/delete/', views.delete_fruit, name='delete_fruit'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/details/', views.profile_details, name='profile_details'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]
