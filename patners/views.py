from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class PartnerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'partners.html')

    def post(sled, request, *args, **kwargs):
        pass