from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # post views
    path('', views.job_offers_list, name='job_offers_list'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
]