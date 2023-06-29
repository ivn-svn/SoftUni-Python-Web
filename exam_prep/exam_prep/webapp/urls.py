from django.urls import path
from exam_prep.webapp import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile_page', views.profile_page, name='profile_page'),
    path('create_album_page', views.create_album_page, name='create_album_page'),
]