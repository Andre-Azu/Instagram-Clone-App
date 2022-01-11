from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Userprofile(models.Model):
    profile_picture=CloudinaryField('image')
    bio = models.CharField(max_length=100)
    username = models.CharField(max_length=15)
    followers = models.IntegerField(default=50)
    following = models.IntegerField(default=12)
    

class Image(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    image =CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=1000)
    comments = models.TextField()
    likes= models.IntegerField(null=True, default=0)
    time_posted = models.DateTimeField(auto_now_add = True)
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()

    def count_likes(self):
       return self.likes.count()

    def update_caption(self, image_caption):
        self.caption = image_caption
        self.save()
    
# class Follows(models.Model):
#     follower = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='following')
#     followed = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='followers')

