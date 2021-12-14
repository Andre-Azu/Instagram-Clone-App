from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from .models import Image
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def homepage_images(request):
    images=Image.objects.all()
    return render(request, 'homepage.html')

#Function login in the user
def user_login(request):
    message = 'Sign In!'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f" Hello, {username} welcome to clicksgram")
            return redirect('homepage')
        else:
            messages.success(request,"sorry,try login in again")
            return render(request,'registration/login.html')
    else:
        return render(request, 'registration/login.html',{"message":message})


def user_signup(request):
    message = 'CREATE ACCOUNT !'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Your account has  succesfully been created!"))
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{"message":message, "form":form})


def user_logout(request):
    logout(request)
    messages.success(request,("You have sussessfully signed out"))
    return redirect('login')