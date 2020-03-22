from django import forms
from .models import Address

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class CheckoutForm(forms.ModelForm):
    shipping_country = CountryField().formfield(
                                    required=False,
                                    widget=CountrySelectWidget(attrs={
                                    'class': 'select__option',}))
    billing_country  = CountryField().formfield(
                                    required=False,
                                    widget=CountrySelectWidget(attrs={
                                    'class': 'select__option',}))

    class Meta:
        model = Address
        fields = ['first_name','last_name','shipping_country','billing_country', 'address','zip_code','phone_num']
