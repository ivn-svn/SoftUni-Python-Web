from django.urls import path
from exam_prep.webapp import views

# . Routes
#    • http://localhost:8000/ - home page
#    • http://localhost:8000/album/add/ - add album page
#    • http://localhost:8000/album/details/<id>/ - album details page
#    • http://localhost:8000/album/edit/<id>/ - edit album page
#    • http://localhost:8000/album/delete/<id>/ - delete album page
#    • http://localhost:8000/profile/details/ - profile details page
#    • http://localhost:8000/profile/delete/ - delete profile page



urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('album/add/', views.create_album_page, name='create_album_page'),
    path('album/details/<int:pk>/', views.album_details_page, name='album_details_page'),
    path('album/edit/<int:pk>/', views.edit_album_page, name='edit_album_page'),
    path('album/delete/<int:pk>/', views.delete_album_page, name='delete_album_page'),
    path('profile/details/', views.profile_page, name='profile_page'),
    path('profile/delete/', views.delete_profile_page, name='delete_profile_page'),
]