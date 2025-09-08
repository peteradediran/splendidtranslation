from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Splits the string by the given argument
    Usage: {{ "a,b,c"|split:"," }}
    """
    return value.split(arg)