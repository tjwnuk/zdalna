from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import Context, Template

from . import helpers
from .models import JobOffer

from .forms import JobOfferForm

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
    offers = JobOffer.objects.all().order_by('-date') # newest offers first
    return render(request, 'all_offers.html', {'offers': offers})

def add_offer(request):
    if not request.user.is_authenticated:
            return HttpResponse('You should login first in order to add job offer.')

    if request.method == 'GET':
        form = JobOfferForm()
        return render(request, 'add_offer.html', { 'form': form })

    else:
        try:
            form = JobOfferForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('all_offers')

        except ValueError:
            return render(request, 'createreview.html', {'form':JobOfferForm(),'error':'bad data passed in'})