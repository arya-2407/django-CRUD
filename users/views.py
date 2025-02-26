from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
# Create your views here.

def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm ()
    return render(req,'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    return redirect('foodapp:item')  # Show a logout confirmation page