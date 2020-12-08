from django.contrib.auth.models import User
from django.db import models

from app.models.validators import max_value_years, min_value, max_value_months, max_value_weeks

PET_CHOICES = (
    ('Dog', 'dog'),
    ('Cat', 'cat'),
    ('Bird', 'bird'),
    ('Other', 'other'),

)


class Pet(models.Model):
    image = models.ImageField(upload_to='Pets')
    years = models.PositiveIntegerField(blank=False, default=0, validators=[max_value_years, min_value])
    months = models.PositiveIntegerField(blank=False, default=0, validators=[max_value_months, min_value])
    weeks = models.PositiveIntegerField(blank=False, default=0, validators=[max_value_weeks, min_value])
    type = models.CharField(choices=PET_CHOICES, blank=False, max_length=10)
    breed = models.CharField(default='Unknown', blank=False, max_length=30)
    description = models.TextField(default=' ')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
