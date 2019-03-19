from django import template

register = template.Library()


@register.filter(name='getposition')
def getposition(value, arg):
    original_string = value
    position = arg
    
    a = original_string.replace('\n\n', '\n').replace('\n', ': ')
    b = a.split(': ')

    try:
        c = b[position]
    except IndexError:
        c = 'N/A'

    return c


@register.filter(name='getlistitem')
def getlistitem(value, arg):
    original_list = value
    position = arg
    
    return original_list[position]
