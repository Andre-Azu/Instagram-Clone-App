from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='instagram',default=None)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=1000)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()