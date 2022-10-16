from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ( 'cust_name', 'organization', 'role', 'bldgroom', 'address', 'city', 'state', 'zipcode',
            'email', 'phone')
