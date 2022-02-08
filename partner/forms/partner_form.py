from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, HTML, Layout, Submit

from partner.models import *

class PartnerForm(ModelForm):
    organisation_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type your Organisation's Name"
    }), label="Organisation's Name")

    contact_person_id = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        "class": "input",
        "type": "number",
        "placeholder": "Enter Contact Person Id"
    }), label="Contact Person ID")

    class Meta:
        model = Partner
        fields = ['organistion_name', 'contact_person', 'partnership_type']
    
    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout = Layout(
            HTML('<h4 class="partner-data mx-auto mt-4 text-center" style="font-family: Times, serif; font-style:italic; color: #2da0f7;"><strong>Partnership Details</strong></h4>'),
            HTML('<hr class="col-md-6 offset-md-3" style="border-top: 0px;">'),
        )
        for field in self.Meta.fields:
            helper.layout.append(
                Field(field, wrapper_class='row text-white m-1'),
            )
        helper.layout.append(
            Div(
                Submit('submit', 'Request for Partnership', style="font-family: Georgia, Times, serif; font-weight: bold;", css_class='btn btn-primary rounded-pill col-md-6 offset-md-3 mb-2'),
            )
        )
        helper.field_class = 'col-md-8'
        helper.label_class = 'col-md-4'
        return helper

    def clean_organisation_name(self):
        org_name = self.cleaned_data.get('organisation_name')

        if len(org_name) < 2:
            raise forms.ValidationError("Your organisation's name is too short")

        return org_name