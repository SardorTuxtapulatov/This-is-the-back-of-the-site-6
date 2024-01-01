from django.shortcuts import render
from django.views.generic import TemplateView

def home_page(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'
class AboutView(TemplateView):
    template_name = 'about.html'
class ServiceView(TemplateView):
    template_name = 'service.html'
class ContactView(TemplateView):
    template_name = 'contact.html'



