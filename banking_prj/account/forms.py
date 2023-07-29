from django import forms
from account.models import KYC
from django.forms import ImageField, FileInput, DateInput


class DateInput(forms.DateInput):
    input_type = 'date'


class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = [
            'full_name',
            'image',
            'martrtial_status',
            'gender',
            'identity_type',
            'identity_image',
            'date_of_birth',
            'country',
            'state',
            'city',
            'zip_code',
            'mobile',
            'fax',
            'date',
            'signature'

        ]
        widgets = {
            'full-name': forms.TextInput(attrs={"placeholder": "Full Name"}),
            'mobile': forms.TextInput(attrs={"placeholder": "Mobile Number"}),
            'fax': forms.TextInput(attrs={"placeholder": "Fax Number"}),
            'country': forms.TextInput(attrs={"placeholder": "Country Name"}),
            'state': forms.TextInput(attrs={"placeholder": "State Name"}),
            'zip_code': forms.TextInput(attrs={"placeholder": "Zip Code"}),
            'city': forms.TextInput(attrs={"placeholder": "City Name"}),
        }
