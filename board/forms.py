from django.forms import ModelForm
from django import forms
from .models import JobOffer

class JobOfferForm(ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    short_description = forms.CharField(label='Short description', required = False, widget=forms.Textarea)
    lower_rate = forms.FloatField(label='Lower rate', required = False)
    upper_rate = forms.FloatField(label='Upper rate', required = False)
    description = forms.CharField(label='Description', max_length=5000, widget=forms.Textarea)
    
    class Meta:
        model = JobOffer
        fields = '__all__'