from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='mip-home'),
    path('team/', views.team, name='mip-team'),
    path('partnership/', views.partner, name='mip-partner'),
    path('donation/', views.donate, name='mip-donation'),
]