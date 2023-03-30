from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitute = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)



class UserActivity(models.Model):

    class ActivityStatus(models.TextChoices):
        LOGGED_IN = "LOGGED_IN"
        LOGGED_OUT = "LOGGED_OUT"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(
        max_length=15,
        choices=ActivityStatus.choices,
        null=True,
    )
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='User Activity'
        verbose_name_plural='     User Activities'

