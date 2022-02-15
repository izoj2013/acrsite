# from os import truncate
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms.donor_registration_form import DonorRegistrationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import reverse, redirect
from .models import Donor

class DonorRegistrationView(SuccessMessageMixin, CreateView):
    model = Donor
    form_class = DonorRegistrationForm
    template_name = 'donor/donor_register.html'
    success_message = 'Thank you for pledging to donate to our Research Trust Fund! Please, Check your email.'

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('mip-home'))


class DonorIndexView(LoginRequiredMixin, ListView):
    context_object_name = 'donors'
    model = Donor
    template_name = 'donor/donors_list.html'
    login_url = 'admin/'

    def get_queryset(self):
        return Donor.objects.all()

    def test_func(self):
        if not self.request.user.is_superuser:
            return reverse_lazy('login_url')

        return redirect('mip-home')


class DonorDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'donor'
    model = Donor
    template_name = 'donor/donor_detail.html'
    login_url = 'admin/'

    def test_func(self):
        if not self.request.user.is_superuser:
            return reverse_lazy('login_url')

        return redirect('mip-home')