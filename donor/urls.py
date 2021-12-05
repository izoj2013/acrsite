from django.urls import path

from . import views

urlpatterns = [
    path('donors', views.DonorIndexView.as_view(), name='donors'),
    path('<int:pk>', views.DonorDetailView.as_view(), name='donor-detail'),
    path('register', views.DonorRegistrationView.as_view(), name='register'),
]