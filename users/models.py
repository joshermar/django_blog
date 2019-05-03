from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override save() with added functionality to resize images.
    # This will ensure that saved images are no larger than 300x300.
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
