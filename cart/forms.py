from django import forms
from cart.models import Order


class CheckoutForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label='First Name*',
                                 widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    last_name = forms.CharField(max_length=50, label='Last Name*',
                                widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    company = forms.CharField(max_length=70, label='Company', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    email = forms.EmailField(label='E-mail*', widget=forms.EmailInput(attrs={'class': 'form-control form-account'}))
    phone = forms.CharField(label='Phone*', max_length=12,
                            widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    address = forms.CharField(label='Address*', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    postcode = forms.CharField(max_length=30, label='PostCode', required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    city = forms.CharField(max_length=30, label='City', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control form-account'}))
    comment = forms.CharField(max_length=200, label='Comment on the order', required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control form-note',
                                                           'placeholder': "Notes about your order, e.g. special notes for delivery."}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'company', 'email', 'phone', 'address',
                  'postcode', 'city', 'comment']
