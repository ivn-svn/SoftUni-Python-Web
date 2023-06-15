from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name="contact page"),
    path('gallery/', views.gallery_view, name="gallery page"),
    path('about/', views.about_view, name="about page"),
]