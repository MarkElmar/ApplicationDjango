from django.urls import path
from .views import (
    ApplicationListView,
    ApplicationDetailView,
    ApplicationCreateView,
    about
)

urlpatterns = [
    path('', ApplicationListView.as_view(), name='application-home'),
    path('app/<pk>', ApplicationDetailView.as_view(), name='application-detail'),
    path('about/', about, name='application-about'),
    path('application/create/', ApplicationCreateView.as_view(), name='application-create')
]
