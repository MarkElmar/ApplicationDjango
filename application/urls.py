from django.urls import path
from . import views
from .views import ApplicationListView, ApplicationDetailView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='application-home'),
    path('application/<pk>', ApplicationDetailView.as_view(), name='application-detail'),
    path('about/', views.about, name='application-about'),
]
