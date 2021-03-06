from django.contrib.auth.models import User
from django.db import models

from app.models.validators import contains_only_digits


class ExtendUser(models.Model):
    phone_number = models.CharField(max_length=10, validators=[contains_only_digits], unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
