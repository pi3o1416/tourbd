
from django import template

register = template.Library()

@register.filter
def limit_letter(value, arg):
    total_letter = len(value)
    if total_letter > arg:
        return value[:arg] + '...'
    return value
