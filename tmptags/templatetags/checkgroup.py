
from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def checkgroup(context, groupname):
    request = context['request']

    group = request.user.groups.filter(name=groupname).exists()
    if group:
        return True
    else:
        return False

