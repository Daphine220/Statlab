from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'