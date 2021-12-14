from django.shortcuts import render
from .models import Image
# Create your views here.
def homepage_images(request):
    # images=Image.objects.all()
    return render(request, 'homepage.html')
