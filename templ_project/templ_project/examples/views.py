import datetime
import random
from templ_project import settings

from django.urls import reverse
from django.shortcuts import render
import random
import glob
import os

# Create your views here.

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


some_student = Student("John", 20)


def index(request):
    context = {
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
    return render(request, 'examples/partials/index.html', context=context)


def contact_view(request):
    return render(request, 'examples/partials/contact.html')


def about_view(request):
    return render(request, 'examples/partials/about.html')



def gallery_view(request):
    photos = glob.glob('static/img/gallery/*.jpg')
    photos = [os.path.basename(photo) for photo in photos]
    return render(request, 'examples/partials/gallery.html', {'photos': photos})