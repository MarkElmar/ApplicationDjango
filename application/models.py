import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Application(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=100)
    companyLocation = models.CharField(max_length=100)
    websiteLink = models.URLField(null=True)
    companyContact = models.CharField(max_length=250)

    class ApplicationWay(models.TextChoices):
        PHONE = 'TE', _('Telefoon')
        EMAIL = 'EM', _('E-mail')
        PERSONAL = 'PE', _('Persoonlijk')

    applicationWay = models.CharField(
        choices=ApplicationWay.choices,
        default=ApplicationWay.EMAIL,
        max_length=50
    )
    dateApplication = models.DateField(null=True)
    dateReaction = models.DateField(null=True)
    dateFaceToFace = models.DateField(null=True)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    reasonRejected = models.TextField(null=True, blank=True)
