from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms.donor_registration_form import DonorRegistrationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import reverse, redirect
from .models import Donor

# Create your views here.
# class DonorLoginView(View):
#     form = DonorRegistrationForm
#     fields = ['email', 'password1']

class DonorRegistrationView(SuccessMessageMixin, CreateView):
    model = Donor
    template_name = 'donor/donor_register.html'
    success_message = 'Thank you for pledging to donate to our Research Trust Fund! Please, Check our email for validation.'
    form_class = DonorRegistrationForm

    def get_success_url(self):
        return self.request.GET.get('next', reverse('mip-home'))


class DonorIndexView(UserPassesTestMixin, ListView):
    context_object_name = 'donors'
    model = Donor
    template_name = 'donor/donors_list.html'

    def get_queryset(self):
        return Donor.objects.all()

    def test_func(self):
        if not self.request.user.is_superuser:
            return redirect('admin/')

        return redirect('mip-home')


class DonorDetailView(UserPassesTestMixin, DetailView):
    context_object_name = 'donor'
    model = Donor
    template_name = 'donor/donor_detail.html'

    def test_func(self):
        if not self.request.user.is_superuser:
            return redirect('admin/')

        return redirect('mip-home')