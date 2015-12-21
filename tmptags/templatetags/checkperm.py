# -*- coding: utf-8 -*-

from django.template import Library

register = Library()

@register.assignment_tag(takes_context=True)
def checkperm(context, permission_name):
    request = context['request']
    if request.user.has_perm(permission_name) == False:
        return False
    return True