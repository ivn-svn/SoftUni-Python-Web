from django.shortcuts import render, redirect
from MyProject_RegularExam.Fruitipedia.models import Profile, Fruit


def index(request):
    return render(request, 'fruitipedia/index.html')


def create_profile(request):
    if request.method == 'POST':
        # Process the profile creation form
        # Save the profile to the database
        return redirect('fruitipedia:dashboard')
    else:
        return render(request, 'fruitipedia/create-profile.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruitipedia/dashboard.html', {'fruits': fruits})


def create_fruit(request):
    if request.method == 'POST':
        # Process the fruit creation form
        # Save the fruit to the database
        return redirect('fruitipedia:dashboard')
    else:
        return render(request, 'fruitipedia/create-fruit.html')


def fruit_details(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    return render(request, 'fruitipedia/details-fruit.html', {'fruit': fruit})


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    if request.method == 'POST':
        # Process the fruit edit form
        # Save the edited fruit to the database
        return redirect('fruitipedia:dashboard')
    else:
        return render(request, 'fruitipedia/edit-fruit.html', {'fruit': fruit})


def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.get(id=fruit_id)
    if request.method == 'POST':
        # Delete the fruit from the database
        return redirect('fruitipedia:dashboard')
    else:
        return render(request, 'fruitipedia/delete-fruit.html', {'fruit': fruit})


def profile_details(request):
    profile = Profile.objects.first()  # Get the profile based on your logic
    return render(request, 'fruitipedia/details-profile.html', {'profile': profile})


def edit_profile(request):
    profile = Profile.objects.first()  # Get the profile based on your logic
    if request.method == 'POST':
        # Process the profile edit form
        # Save the edited profile to the database
        return redirect('fruitipedia:profile_details')
    else:
        return render(request, 'fruitipedia/edit-profile.html', {'profile': profile})


def delete_profile(request):
    profile = Profile.objects.first()  # Get the profile based on your logic
    if request.method == 'POST':
        # Delete the profile and associated fruits from the database
        return redirect('fruitipedia:index')
    else:
        return render(request, 'fruitipedia/delete-profile.html', {'profile': profile})
