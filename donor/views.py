from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from .forms.donor_registration_form import DonorRegistrationForm
from . import models

# Create your views here.
class DonorLoginView(View):
    form = DonorRegistrationForm
    fields = ['email', 'password1']
    pass

class DonorRegistrationView(SuccessMessageMixin, CreateView):
    model = models.Donor
    template_name = 'donor/donor_registration.html'
    success_msg = 'Thank you for signing up as a Donor to Research Trust Fund! We will be in touch.'
    #form = DonorRegistrationForm
    fields = '__all__'

class DonorIndexView(ListView):
    context_object_name = 'donors'
    template_name = 'donor/donors_list.html'

    def get_queryset(self):
        return models.Donor.objects.all()

class DonorDetailView(DetailView):
    context_object_name = 'donor'
    model = models.Donor
    template_name = 'donor/donor_detail.html'