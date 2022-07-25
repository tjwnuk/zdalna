from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import Context, Template

from . import helpers
from .models import JobOffer

# Create your views here.

def home(request):

    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About site</h1> \n This is about site')

def offer(request, offer_id):
    offer = get_object_or_404(JobOffer, pk=offer_id)
    context = {
        'title': offer.title,
        'offer': offer,
    }
    return render(request, 'offer.html', context)

def all_offers(request):

    offers = JobOffer.objects.all()

    return render(request, 'all_offers.html', {'offers': offers})