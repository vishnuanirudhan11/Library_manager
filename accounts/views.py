from django.contrib.auth.models import auth
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.

def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': "username"})
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            gender = request.POST.get('gender')
        except MultiValueDictKeyError:
            return render(request,'register.html',{'error':"keyerror"})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': "email"})
        elif password1 != password2:
            return render(request, 'register.html', {'error': "pswd"})
        else:
            s=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,
                                       password=password1,gender=gender)
            s.save()
            user=auth.authenticate(email=email,password=password1)
            auth.login(request,user)
            return redirect('home')
    return render(request,'register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    email=request.POST.get('email')
    password = request.POST.get('password')
    user = auth.authenticate(email=email, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('home')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
