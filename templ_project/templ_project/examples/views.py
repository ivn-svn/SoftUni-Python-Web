import datetime
import random

from django.shortcuts import render
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
    context = {
        "title": "Home",
        "random_int": random.random(),
        "nested": {
            "second": "second value"
        },
        "student": some_student.get_age(),
        "now": datetime.datetime.now(),
    }
    return render(request, 'examples/index.html', context=context)
