from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import  UserForm
from django.http import HttpResponseRedirect

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:           #logout when you start again
        logout(request)
        form = UserForm(request.POST or None)
        context = { 
            "form": form,
        }
        return render(request, 'music/login.html', context)
        
       

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = { 
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('https://azouaoui-med.github.io/pro-sidebar-template/src/')
             
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
              
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


