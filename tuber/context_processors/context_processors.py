import contactinfo
from contactinfo.models import Contactinfo

# Create your views here.

def contactinfo(request):
    contact = Contactinfo.objects.order_by("-created_date")[:1]

    return {
        'contact' : contact
    }