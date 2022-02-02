from django.urls import path

from . import views

urlpatterns = [
    path('donors', views.DonorIndexView.as_view(), name='mip-donors'),
    path('<int:pk>', views.DonorDetailView.as_view(), name='mip-donor-detail'),
    path('register', views.DonorRegistrationView.as_view(), name='mip-register'),
]