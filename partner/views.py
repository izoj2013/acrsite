from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, resolve_url, render
from .forms.partner_form import PartnerForm
from .models import Partner

# Create your views here.
class PartnerCreateView(SuccessMessageMixin, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/partner_create.html'
    success_message = 'Thank you for wanting to partner with us! We will get in touch with you soon.'

    def get_success_url(self) -> str:
        return self.request.GET.get('mip-home')


class PartnerDetailView(DetailView):
    context_object_name = 'partner'
    model = Partner
    template_name = 'partner/partner_detail.html'


class PartnerListView(ListView):
    context_object_name = 'partners'
    model = Partner
    template_name = 'partner/partner_list.html'

    def get_queryset(self):
        return Partner.objects.all()
