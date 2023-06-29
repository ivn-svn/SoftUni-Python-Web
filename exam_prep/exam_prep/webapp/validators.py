from django.core.exceptions import ValidationError


class TextContainsOnlyAlphaNumericAndUnderscoreValidator:
    def __call__(self, value):
        if not value.isalnum() and '_' not in value
            raise ValidationError('Only alpha-numeric characters and underscores are allowed.')

    def __eq__(self, other):
        return True