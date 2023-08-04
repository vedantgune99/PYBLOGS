from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.PositiveBigIntegerField(null=True)
    profile_pic = models.ImageField(
        upload_to='profiles/', default="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp")

    def __str__(self):
        return str(self.user)
