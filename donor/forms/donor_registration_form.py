from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, HTML, Submit
from mipweb.utils import is_valid_string, is_valid_email

from donor.models import *

class DonorRegistrationForm(ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Your Name"
    }), label='Name')

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Type Email Address"
    }), label='Email')

    organisation_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Your Organisation"
    }), label="Organisation's Name")

    pledge_amount = forms.DecimalField(required=True, min_value=10, decimal_places=2, label="Pledge Amount")

    class Meta:
        model = Donor
        fields = ['name', 'email', 'organisation_name', 'donor_type', 'pledge_amount']

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout = Layout(
            HTML('<h5 class="pledge-title mx-auto mt-2 text-center" style="font-family: Times, serif; font-style: italic; color: #D6580F;"><strong>Pledge your Donation</strong></h5>'),
            HTML('<hr class="col-md-4 offset-md-4" style="border-top: 0px;">'),
        )
        for field in self.Meta().fields:
           helper.layout.append(
              Field(field, wrapper_class='row text-white m-1'),
           )
        helper.layout.append(
            Div(
                Div(css_class='col-md-4'),
                Div(Submit('submit', 'Submit Pledge', style="font-family: Georgia, Times, serif; font-weight: bold;", css_class='btn btn-primary rounded-pill col-md-6 offset-md-3 col-sm-2 offset-sm-5 mb-3'),)
            )
        )
        helper.field_class = 'col-md-9'
        helper.label_class = 'col-md-3'
        return helper


    def clean_name(self):
        donor_name = self.cleaned_data.get('name')

        if is_valid_string(donor_name):
            if len(donor_name) < 2:
                raise forms.ValidationError("Your name is too short")

        return donor_name


    def clean_email(self):
        email_addr = self.cleaned_data.get('email')

        if is_valid_email(email_addr):
            return email_addr

        raise forms.ValidationError("Invalid email address")


    def clean_organisation_name(self):
        org_name = self.cleaned_data.get('organisation_name')

        if is_valid_string(org_name):
            if len(org_name) < 2:
                raise forms.ValidationError("Your organisation's name is too short")

        return org_name