from django import forms
from .models import Order

class PaymentForm(forms.Form):
    # assign values to variables month / year choices
    MONTH_CHOICES = [(i, i) for i in range (1, 13)]
    YEAR_CHOICES = [(i, i) for i in range (2018, 2050)]
    
    # create payment form fields with required eqt false for server-side security
    credit_card_number = forms.CharField(label='credit card number', required=False)
    cvv = forms.CharField(label='security code (cvv)', required=False)
    expiry_month = forms.ChoiceField(label='month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='month', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
