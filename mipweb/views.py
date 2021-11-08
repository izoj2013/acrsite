from django.shortcuts import render
from .donor_form import DonorForm

# Create your views here.


def home(request):
    return render(request, 'mipweb/home.html')

def team(request):
    return render(request, 'mipweb/mip-team.html')

def partner(request):
    return render(request, 'mipweb/partnership.html')

def donate(request):
    form = DonorForm()
    return render(request, 'mipweb/donation_form.html', {'form': form})
