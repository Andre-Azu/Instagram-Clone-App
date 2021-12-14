from django.shortcuts import render
from .models import Image
# Create your views here.
def all_images(request):
    images=Image.objects.all()
    return render(request, 'home.html', {'images':images })
