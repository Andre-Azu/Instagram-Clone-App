from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# from django.conf.urls import url


urlpatterns = [
    path('', views.user_login,name='homepage'),
    path('login',views.user_login,name='login'),
    path('signup',views.user_signup, name='signup'),
    path('profile', views.my_profile,name='profile'),
    path('new/image', views.new_image, name='new_image' ),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
