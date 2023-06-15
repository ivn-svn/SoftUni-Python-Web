import datetime
import random
from django.urls import reverse


from django.shortcuts import render, redirect
from . import views
import random
# Create your views here.
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


some_student = Student("John", 20)


def index(request):
    contact_url = reverse('contact page')
    gallery_url = reverse('gallery page')
    about_url = reverse('about page')
    context = {
        'contact_url': contact_url,
        'gallery_url': gallery_url,
        'about_url': about_url,
        "title": "Home",
        "random_int": random.random(),
        "nested": {
            "second": "second value",
        },
        "student_age": some_student.get_age(),
        "students": ["Kalin", "Ivan", "Pesho", "Мартин", "Mariya"],
        "students_second": [],
        "now": datetime.datetime.now(),
        "numbers": [1, 2, 3, 4, 5, 6, 7],
        "name": "Now hardcoded",
        "students_obj": [
            Student('Lili', 23),
            Student('Moni', 20),
            Student('Yavor', 30)
        ],
        "logged_in": True
    }
    # context + template = HtmlResponse('<html>...</html>')
    return render(request, 'examples/partials/index.html', context=context)


def contact_view(request):
    return render(request, 'examples/contact.html')

def about_view(request):
    return render(request, 'examples/partials/about.html')

def gallery_view(request):
    photos = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png",
        "https://upload.wikimedia.org/wikipedia/commons/c/cd/Adjahoui.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Asim_Mukhopadhyay_with_Sir_Erlardso.jpg/1280px-Asim_Mukhopadhyay_with_Sir_Erlardso.jpg"
    ]
    return render(request, 'examples/gallery.html', {'photos': photos})