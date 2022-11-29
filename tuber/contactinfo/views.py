from django.shortcuts import render
from .models import Contactinfo

# Create your views here.

def contactinfo(request):
    contact = Contactinfo.objects.order_by("-created_date")

    data = {
        'contact' : contact
    }
    return render(request, 'includes/footer.html', data)