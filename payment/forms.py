from django import forms
from .models import Payment


class PaymentFinancialsForm(forms.Form):
    # create fields to take in financial details for stripe payment
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class PaymentForm(forms.ModelForm):
    # create fields to take in personal details of payment
    class Meta:
        model = Payment
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'country')
        