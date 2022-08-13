from django.shortcuts import render,redirect
from accounts.urls import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html', context)
    else:
        return redirect('/')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/') 

def signup_view(request):
    return render(request, 'accounts/sign-up.html')