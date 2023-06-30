from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
import exam_prep.webapp.validators as validators

# • Profile
#     o Username
#         ▪ Character field, required.
#         ▪ It should have at least 2 characters and a maximum of 15 characters.
#         ▪ The username can consist only of letters, numbers, and an underscore ("_"). Otherwise, raise a ValidationError with the message: "Ensure this value contains only letters, numbers, and underscore."
#     o Email
#         ▪ Email field, required.
#     o Age
#         ▪ Integer field, optional.
#         ▪ The age cannot be below 0.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(15),
            validators.TextContainsOnlyAlphaNumericAndUnderscoreValidator()
        ]
    )
    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(null=True, validators=[validators.validate_non_negative])

    # or ::: age = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.username

class Album(models.Model):
    # • Album
    # o Album Name
    # ▪ Character field, required.
    # ▪ All album names must be unique.
    # ▪ It should consist of a maximum of 30 characters.
    # o Artist
    # ▪ Character field, required.
    # ▪ It should consist of a maximum of 30 characters.
    # o Genre
    # ▪ Char field, required.
    # ▪ It should consist of a maximum of 30 characters.
    # ▪ The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music",
    # "Country Music", "Dance Music", "Hip Hop Music", and "Other".
    # o Description
    # ▪ Text field, optional.
    # o Image URL
    # ▪ URL field, required.
    # o Price
    # ▪ Float field, required.
    # ▪ The number of decimal places of the price should not be specified in the database.
    # ▪ The price cannot be below 0.0.
    # Note: the validations will be examined only by the user side, not the admin side.

    album_name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    artist = models.CharField(max_length=30, blank=False, null=False)
    genre = models.CharField(max_length=30, blank=False, null=False, choices=(
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")
    ))
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False, validators=[validators.validate_non_negative])

    def __str__(self):
        return self.album_name


# Album
# o Album Name
# ▪ Character field, required.
# ▪ All album names must be unique.
# ▪ It should consist of a maximum of 30 characters.
# o Artist
# ▪ Character field, required.
# ▪ It should consist of a maximum of 30 characters.
# o Genre
# ▪ Char field, required.
# ▪ It should consist of a maximum of 30 characters.
# ▪ The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music",
# "Country Music", "Dance Music", "Hip Hop Music", and "Other".
# o Description
# ▪ Text field, optional.
# o Image URL
# ▪ URL field, required.
# o Price
# ▪ Float field, required.
# ▪ The number of decimal places of the price should not be specified in the database.
# ▪ The price cannot be below 0.0.
# Note: the validations will be examined only by the user side, not the admin side.
