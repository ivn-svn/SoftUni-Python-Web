from django.urls import path, include
from .views import register_user, login_user, profile_details, profile_edit, profile_delete

urlpatterns = [
    # localhost:8000/accounts/register
    path('register/', register_user, name="register_user"),
    path('login/', login_user, name="login_user"),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path('delete/', profile_delete, name='profile_delete')
    ])),
]
