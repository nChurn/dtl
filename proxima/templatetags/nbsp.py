from django import template
from django.utils.safestring import mark_safe
from pyparsing import basestring

register = template.Library()

@register.filter()
def brtitle(value):
    return mark_safe(" ".join(value.split('<br>')))

@register.filter()
def nbspstrip(value):
    return mark_safe("&nbsp;".join(value.split('&amp;nbsp;')))

@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, basestring):
        return text.startswith(starts)
    return False
