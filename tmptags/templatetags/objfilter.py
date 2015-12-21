
# -*- coding: utf-8 -*-

from django import template
from django.apps import apps

register = template.Library()

@register.assignment_tag(takes_context=True)
def objfilter(context, **kwargs):

    app = kwargs['app']
    model_name = kwargs['model']
    model = apps.get_model(app, model_name)
    qkwargs = {}
    model_fields = model._meta.fields
    filter_fields = [field for field in model_fields if field.name in kwargs.keys()]
    for key in kwargs.keys():
        if '__' in key:
            for field in model_fields:
                if field.name == key.split('__')[0]:
                    qkwargs[field.name+'__'+key.split('__')[1]] = kwargs.get(key)
    for field in filter_fields:
        qkwargs[field.name] = kwargs.get(field.name)
    return model.objects.filter(**qkwargs)














