from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, resolve_url, render
from .forms.partner_form import PartnerForm
from .models import Partner

# Create your views here.
class PartnerCreateView(SuccessMessageMixin, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/partner_create.html'
    success_message = 'Thank you for wanting to partner with us! We will get in touch with you soon.'

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('mip-home'))


class PartnerDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'partner'
    model = Partner
    template_name = 'partner/partner_detail.html'
    login_url = 'admin/'

    def test_func(self):
        if not self.request.user.is_superuser:
            return reverse_lazy('login_url')

        return redirect('mip-home')

class PartnerListView(LoginRequiredMixin, ListView):
    context_object_name = 'partners'
    model = Partner
    template_name = 'partner/partners_list.html'
    login_url = 'admin/'

    def get_queryset(self):
        return Partner.objects.all()

    def test_func(self):
        if not self.request.user.is_superuser:
            return reverse_lazy('login_url')

        return redirect('mip-home')
