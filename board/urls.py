from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about),
    path('offer', offer),
    path('offer/<id>', offer, name='offer'),
    path('all_offers/', all_offers, name='all_offers')
]