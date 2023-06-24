from django.db import models
"""
You will need 2 models:
    • Profile Model
        ◦ First Name
            ▪ Character field, required.
            ▪ It should consist of a maximum of 25 characters and a minimum of 2 characters.
            ▪ The first name must start with a letter. Otherwise raise ValidationError with the following message: "Your name must start with a letter!"
        ◦ Last Name
            ▪ Character field, required.
            ▪ It should consist of a maximum of 35 characters and a minimum of 1 character.
            ▪ The last name must start with a letter. Otherwise raise ValidationError with the following message: "Your name must start with a letter!"
        ◦ Email
            ▪ Email field, required.
            ▪ It should consist of a maximum of 40 characters.
        ◦ Password
            ▪ Character (password) field, required.
            ▪ It should consist of a maximum of 20 characters and a minimum of 8 characters.
        ◦ Image URL
            ▪ URL field, optional.
        ◦ Age
            ▪ Integer field, optional.
            ▪ The age default value should be 18.

    • Fruit Model
        ◦ Name
            ▪ Character field, required.
            ▪ It should consist of a maximum of 30 and a minimum of 2 characters.
            ▪ The name should contain only letters. Otherwise raise a ValidationError with the following message: "Fruit name should contain only letters!"
        ◦ Image URL
            ▪ URL field, required.
        ◦ Description
            ▪ Text field, required.
        ◦ Nutrition
            ▪ Text field, optional.
"""
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError


class Profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
    image_url = models.URLField(blank=True)
    age = models.IntegerField(default=18)

    def clean(self):
        if not self.first_name[0].isalpha():
            raise ValidationError("Your name must start with a letter!")
        if not self.last_name[0].isalpha():
            raise ValidationError("Your name must start with a letter!")


class Fruit(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(blank=True)

    def clean(self):
        if not self.name.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
