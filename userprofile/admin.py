from django.contrib import admin
from django.db.models.fields import FilePathField
from .models import Userprofile,Follows

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Follows)