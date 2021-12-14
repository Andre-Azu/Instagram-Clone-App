from django.shortcuts import render
from .models import Userprofile, Follows
# Create your views here.
def my_profile(request):
    
    return render(request, 'profile.html')