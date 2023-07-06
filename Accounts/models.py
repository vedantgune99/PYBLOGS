from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.PositiveBigIntegerField(null=True)
    profile_pic = models.ImageField(
        upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return str(self.user)
