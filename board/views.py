from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import JobOffer

# Create your views here.

def job_offers_list(request):
    offers = JobOffer.objects.all()
    
    return render(request,
                  'job_offers/detail.html',
                  {'offers': offers })