from django import forms

class PartnerForm(forms.Form):
    firt_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    organisation_name = forms.CharField(max_length=256)