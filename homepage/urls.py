from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url


urlpatterns = [
    path('', views.homepage_images,name='home'),
    path('login',views.user_login,name='login'),
    path('signup',views.user_signup, name='signup')
]