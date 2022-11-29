from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from hiretubers.models import Hiretuber
from django.core.mail import send_mail
# from tuber.settings import EMAIL_HOST_USER


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Checking if username and email already exists
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()

                    # # Sending welcome mail
                    # subject = 'Welcome mail'
                    # message = 'Welcome to YTuber app. Enjoy your collaborations!'
                    # recepient = str(email)
                    # send_mail(subject, 
                    #     message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                    return redirect('login')
        else:
            messages.warning(request, 'Passwords do not match')
            return redirect('register')

    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    tubers = Hiretuber.objects.filter(email=request.user.email)
    creator = Hiretuber.objects.filter(tuber_email=request.user.email)
    data = {
        'tubers': tubers,
        'creator':creator,
        'user_id': request.user.id
    }

    return render(request,'accounts/dashboard.html', data)