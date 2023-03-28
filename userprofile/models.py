from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitute = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    