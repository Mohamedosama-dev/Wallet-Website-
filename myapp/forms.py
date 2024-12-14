from django import forms
from .models import Charity
from .models import Service

class CharityTransferForm(forms.Form):
    charity = forms.ModelChoiceField(queryset=Charity.objects.all(), empty_label="Select Charity")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)

class ServicePaymentForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), empty_label="Select a Service")
    service_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(decimal_places=2)