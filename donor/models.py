from email.policy import default
from enum import unique
from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils.translation import gettext_lazy as _
from mipweb.utils import add_time

# Create your models here.

@unique
class DonorType(models.TextChoices):
    INDIVIDUAL = 'Individual Donor', 'individual-donor'
    ORGANISATION = 'Group Donorr', 'group-donor'

@unique
class PledgeStatus(models.TextChoices):
    NOT_HONOURED = 'Not-Honoured Pledge', 'not-honoured-pledge', 
    HONOURED = 'Honoured Pledge', 'honoured-pledge'

class Donor(models.Model):

    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(unique=True, blank=False)
    donor_type = models.CharField(max_length=64, choices=DonorType.choices, default=DonorType.INDIVIDUAL)
    organisation_name = models.CharField(max_length=64, blank=False)
    pledge_amount = models.FloatField(blank=False)
    pledge_date = models.DateField(auto_now_add=True)
    pledge_status = models.CharField(max_length=64, choices=PledgeStatus.choices, default=PledgeStatus.NOT_HONOURED)
    received_amount = models.FloatField(default=0.0)
    receipt_date = models.DateTimeField(default=add_time(3))

    def __str__(self) -> str:
        return self.name

    def is_individiual_donor(self):
        return self.donor_type == DonorType.INDIVIDUAL

    def is_group_donor(self):
        return self.donor_type == DonorType.ORGANISATION

    def is_pledge_honoured(self):
        return self.pledge_status == PledgeStatus.HONOURED

    def has_pledge_failed(self):
        return self.pledge_status == PledgeStatus.NOT_HONOURED
