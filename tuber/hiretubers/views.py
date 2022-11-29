from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hiretuber
from django.shortcuts import get_object_or_404

# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_name = request.POST['tuber_name']
        tuber_id = request.POST['tuber_id']
        tuber_email = request.POST["tuber_email"]
        user_id = request.POST['user_id']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        details = request.POST['details']

        # TODO : Do all sanitization(eg: check first_name, last_name , email, phone everything is in format and all)
        hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_name=tuber_name,
        tuber_id=tuber_id,tuber_email=tuber_email,user_id=user_id,email=email,phone=phone,city=city,state=state,details=details)

        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('home')

def updatestatus(request,id):
    hiretuber = get_object_or_404(Hiretuber, id=id)
    tubers = Hiretuber.objects.filter(email=request.user.email)
    creator = Hiretuber.objects.filter(tuber_email=request.user.email)
    data = {
        'tubers': tubers,
        'creator':creator,
        'user_id': request.user.id
    }

    if request.method=='POST':
        status = request.POST.get('status', 'Screening')
        hiretuber.status = status
        hiretuber.save()
        return render(request,'accounts/dashboard.html', data)