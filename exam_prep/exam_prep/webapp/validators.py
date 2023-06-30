from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class TextContainsOnlyAlphaNumericAndUnderscoreValidator:
    pattern = r'^[a-zA-Z0-9_]+$'

    def __call__(self, value):
        if not re.match(self.pattern, value):
            raise ValidationError('Only alpha-numeric characters and underscores are allowed.')

    def __eq__(self, other):
        return isinstance(other, self.__class__)


def validate_non_negative(value):
    if value < 0:
        raise ValidationError("The age cannot be below 0.")
