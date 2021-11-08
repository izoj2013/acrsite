from django import forms
from django.db.models import fields
from .models import Donor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('donate', 'Submit Your Pledge'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-danger'))