from django.urls import path
from .views import HomeView, AboutView, ServiceView,ContactView

app_name = 'freg'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('service/', ServiceView.as_view(), name="service_page"),
    path('contact/', ContactView.as_view(), name='contact_page'),
]



























