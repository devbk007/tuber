from django.shortcuts import render
from .models import Slider, Team, About, Services, Chooseus
from youtubers.models import Youtuber

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Youtuber.objects.order_by("-created_date")
    
    data = {
        'sliders': sliders,
        'team': team,
        'featured_youtubers' : featured_youtubers,
        'youtubers' : youtubers,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    team = Team.objects.order_by("-created_date")
    content = About.objects.order_by("-created_date")
    data = {
        'team': team,
        'content': content
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    services = Services.objects.order_by("created_date")
    chooseus = Chooseus.objects.order_by("-created_date")
    data = {
        "services" : services,
        "chooseus" : chooseus
    }
    return render(request, 'webpages/services.html', data)

def contact(request):
    return render(request, 'webpages/contact.html')