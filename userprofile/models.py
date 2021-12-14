from django.db import models

# Create your models here.
class Userprofile(models.Model):
    profile_picture=models.ImageField(upload_to='instagram_profile/', default = None)
    bio = models.CharField(max_length=100)
    username = models.CharField(max_length=15)

class Follows(models.Model):
    follower = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='followers')


