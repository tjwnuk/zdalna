from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from . import helpers

# Create your views here.

def home(request):

    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About site</h1> \n This is about site')

def view_offer(request):
    context = {
        'title': "Offer details"
    }
    return render(request, 'offer.html', context)