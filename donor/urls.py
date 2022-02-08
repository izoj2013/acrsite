from django.urls import path
# from django.contrib.admin.views.decorators import login_required

from . import views

urlpatterns = [
    path('donors', views.DonorIndexView.as_view(), name='mip-donors'),
    path('donor/<int:pk>', views.DonorDetailView.as_view(), name='mip-donor-detail'),
    path('donor', views.DonorRegistrationView.as_view(), name='mip-donor'),
]