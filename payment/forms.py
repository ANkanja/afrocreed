from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}), required=True)
    shipping_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line 1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line 2'}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
    shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}), required=False)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

        exclude = ['user',]


class PaymentForm(forms.Form):
    card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name on Card'}), required=True)
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Card Number'}), required=True)
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'MM/YY'}), required=True)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CVC'}), required=True)
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}), required=True)
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)
    card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
    card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line 1'}), required=True)
    card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line 2'}), required=False)