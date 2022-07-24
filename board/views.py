from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

from . import helpers
from .models import JobOffer

# Create your views here.

def home(request):

    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About site</h1> \n This is about site')

def offer(request, id=None):

    offer_id = id

    offer = JobOffer.objects.get(id=offer_id)

    context = {
        'title': offer.title,
        'offer': offer,
    }
    return render(request, 'offer.html', context)

def all_offers(request):

    offers = JobOffer.objects.all()

    return render(request, 'all_offers.html', {'offers': offers})