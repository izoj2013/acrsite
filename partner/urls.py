from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('partners', views.PartnerListView.as_view(), name='mip-partners'),
    path('partner<int:pk>', views.PartnerDetailView.as_view(), name='mip-partner-detail'),
    path('partner', views.PartnerCreateView.as_view(), name='mip-partner'),
]