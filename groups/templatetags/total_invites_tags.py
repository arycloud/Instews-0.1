from django import template

register = template.Library()


@register.simple_tag
def add_invites(a, b):
    return a+b
