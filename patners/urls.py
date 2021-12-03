from django.urls import path

from . import views

urlpatterns = [
    path('', views.PartnerView.as_view(), name='partner')
]