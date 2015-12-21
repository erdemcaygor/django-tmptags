from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View
from .models import *

class index(View):

    def get(self, request):

        return render_to_response('index.html', locals())