from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # post views
    path('', views.index, name='index'),
    path('offers/', views.job_offers_list, name='job_offers_list'),
    path('offer/<int:id>/', views.offer_detail, name='offer_detail'),
]