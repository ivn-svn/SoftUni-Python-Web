from django.shortcuts import render

from exam_prep.webapp.models import Profile


# Create your views here.


def home_page(request):
    profile = Profile.objects.first()  # Assigning the first Profile object to the variable 'profile'
   # profile = "rofile.objects.first()" # Assigning the first Profile object to the variable 'profile'

    # TODO: check template!
    context = {
        'profile': profile,
    }
    return render(request, "home-no-profile.html", context)


def profile_page(request):
    return render(request, 'profile-details.html')

def create_album_page(request):
    return render(request, 'add-album.html')
def delete_profile_page(request):
    return render(request, 'profile-delete.html')

def edit_album_page(request):
    return render(request, 'edit-album.html')

def delete_album_page(request):
    return render(request, 'delete-album.html')

def album_details_page(request):
    return render(request, 'album-details.html')