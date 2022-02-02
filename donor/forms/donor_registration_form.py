# from django.db.models import fields
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, HTML, Submit

from donor.models import Donor

class DonorRegistrationForm(ModelForm):
    
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type First Name"
    }), label='First Name')

    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Middle Name"
    }), label='Middle Name')

    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Last Name"
    }), label='Last Name')

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Email"
    }), label='Email')

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Password"
    }), label='Password')

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Confirm Password"
    }), label='Confirm Password')

    organisation = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Type Organisation"
    }), label='Organisation')

    class Meta:
        model = Donor
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2', 'organisation']

    @property
    def helper(self):
        helper = FormHelper(self)
        helper.layout = Layout(
            HTML('<h5 class="register-title mx-auto text-center"><strong>Donor Sign Up</strong></h5>'),
            HTML('<hr class="col-md-4 offset-md-4" style="border-top: 0px">'),
        )
        for field in self.Meta().fields:
           helper.layout.append(
              Field(field, wrapper_class='row'),
           )
        helper.layout.append(
            Div(
                Submit('submit', 'Register', css_class='btn-success'),
                css_class='col-md-2 offset-md-5'
            ))
        helper.field_class = 'col-md-9'
        helper.label_class = 'col-md-3'
        return helper