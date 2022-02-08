from django.shortcuts import render
from donor.forms.donor_registration_form import DonorRegistrationForm

# Create your views here.


def home(request):
    return render(request, 'mipweb/home.html')

def team(request):
    return render(request, 'mipweb/mip-team.html')

def partner(request):
    return render(request, 'mipweb/partnership.html')

def donate(request):
    form = DonorRegistrationForm()
    return render(request, 'mipweb/donation_form.html', {'form': form})
