from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import JobOffer

# Create your views here.

def index(request):
    # index page, front page, home page

    # return HttpResponse('Elo, this is main page')

    return render(request,
                  'board/index.html',
                  {})

def job_offers_list(request):
    """
    List of all job offers
    """
    offers = JobOffer.objects.all()
    
    return render(request,
                  'board/offers_list.html',
                  {'offers': offers })

def offer_detail(request, id):
    """
    Details view of specific job offer
    """

    offer = get_object_or_404(JobOffer, id=id)
    return render(request, 'board/detail.html', {'offer': offer})