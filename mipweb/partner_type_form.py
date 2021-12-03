from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

PARTNERSHIPS = (
    ('', 'Choose...')
    ('COLLABORATION', 'Collaborate with Us')
    ('DEMO', 'Request for a Demo')
    ('DONATION', 'Donate - Research Trust Fund')
    ('HIRE', 'Hire our Services')
    ('', 'Choose...')
)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
    
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput())
