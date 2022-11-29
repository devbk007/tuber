from django.shortcuts import redirect
from django.contrib import messages
from .models import Contactform

# Create your views here.

def contactform(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        details = request.POST['details']

        contactform = Contactform(full_name=full_name,phone=phone,email=email,company_name=company_name,subject=subject,
            details=details)
        contactform.save()

        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')