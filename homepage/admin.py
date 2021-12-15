from django.contrib import admin
from .models import Image,Userprofile
# Register your models here.
admin.site.register(Image)
admin.site.register(Userprofile)
# admin.site.register(Follows)