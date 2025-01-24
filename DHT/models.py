from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)



class Incident(models.Model):
    # class
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    reported_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title

    class Meta:
        db_table = "incidents"



class NotificationType(models.TextChoices):
    SMS = "SMS", "SMS"
    TELEGRAM = "TELEGRAM", "TELEGRAM"
    EMAIL = "EMAIL", "EMAIL"
    WHATSAPP = "WHATSAPP", "WHATSAPP"


class NotificationsParameters(models.Model):
    mainResource = models.TextField(null=False)
    type = models.CharField(max_length=10, choices=NotificationType.choices, null=False)
    created_at = models.DateTimeField(auto_now_add=True, primary_key=False)

    class Meta:
        db_table = "notifications_parameters"
        constraints = [
            models.UniqueConstraint(
                fields=["type", "mainResource"], name="unique_type_resource"
            )
        ]
