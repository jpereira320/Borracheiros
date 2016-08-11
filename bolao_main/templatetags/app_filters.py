from django import template

register = template.Library()


@register.filter(name='getposition')
def getposition(value, arg):
    original_string = value
    position = arg
    
    a = original_string.replace('\n\n', '\n').replace('\n', ': ')
    b = a.split(': ')
    return b[position]



