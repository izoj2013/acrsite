from dataclasses import fields
from sqlite3 import Row
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Field, HTML, Layout, Row, Submit

from mipweb.utils import get_cleaned_attribute, is_valid_email

from partner.models import *

class PartnerForm(ModelForm):
    organisation_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type your Organisation's Name"
    }), label="Organisation's Name")

    contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Corporate Email Address"
    }), label='Corporate Email')

    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "name": "body",
        "rows": "5",
        "cols": "7",
        "placeholder": "Describe your partnership request"
    }), label="Partnership Description")

    class Meta:
        model = Partner
        fields = ['organisation_name', 'contact_email', 'partnership_type', 'description']
    
    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout = Layout(
            HTML('<h4 class="partner-data mx-auto mt-4 text-center" style="font-family: Times, serif; font-style:italic; color: #D6580F;"><strong>Partnership Request</strong></h4>'),
            HTML('<hr class="col-md-6 offset-md-3" style="border-top: 0px;">'),
        )
        for field in self.Meta.fields:
            helper.layout.append(
                Field(field, wrapper_class='row text-white m-1'),
            )
        helper.layout.append(
            Div(
                Row(
                    Column(css_class='col-md-4'),
                    Column(
                           Submit('submit', 'Apply for Partnership', style="font-family: Georgia, Times, serif; font-weight: bold;", css_class='btn btn-primary rounded-pill col-md-8 offset-md-2 col-sm-4 offset-sm-4 mb-3'),
                           css_class='col-md-8'
                    )
                )
            )
        )
        helper.field_class = 'col-md-8'
        helper.label_class = 'col-md-4'
        return helper


    def clean_organisation_name(self):
        org_name = self.cleaned_data.get('organisation_name')

        if len(org_name) == 0:
            raise forms.ValidationError("Your organisation's name must not be blank")

        return org_name


    def clean_contact_email(self):
        contact_email = self.cleaned_data.get('contact_email')

        if is_valid_email(contact_email):
            return contact_email

        raise forms.ValidationError("Invalid email address")


    def clean_partnership(self):
        partnership_type = self.cleaned_data.get('partnership_type')

        if partnership_type:
            return partnership_type

        raise forms.ValidationError("Partnership type must not be blank")


    def clean_partnership_descr(self):
        partnership_descr = self.clean_data.get('description')

        if partnership_descr:
            return partnership_descr

        raise forms.ValidationError("Partnership description must not be blank")