from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about),
    path('offer', offer),
    path('offer/<int:offer_id>', offer, name='offer'),
    path('all_offers/', all_offers, name='all_offers'),
    path('add/', add_offer, name='add_offer')
]