from django import template

register = template.Library()

@register.filter(name='odd')
def odd(list_numbers):
    """Custom filter for finding odd numbers. Returns a list of odd numbers."""
    return [x for x in list_numbers]