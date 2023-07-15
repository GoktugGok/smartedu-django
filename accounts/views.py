from django.shortcuts import render , redirect
from . forms import LoginForm , RegisterForm
from django.contrib.auth import authenticate, logout , login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username , password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                
                else:
                    messages.info(request, 'Disable Account')
            
            else:
                 messages.info(request, 'Check Your Username and Password')
    
    else:
        form = LoginForm()
    
    return render(request,'login.html',{'form': form})


def user_register(request):
    return render(request,'register.html')

def user_dashboard(request):
    pass

def user_logout(request):
    pass


