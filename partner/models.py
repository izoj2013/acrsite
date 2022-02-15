from django.db import models
from email.policy import default
from enum import unique
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField

from mipweb.utils import full_name, add_time

# Create your models here.
@unique
class ProjectStatus(models.TextChoices):
    STARTING = 'Start', 'start'
    STARTED = 'Starting', 'starting'
    IN_PROGRESS = 'In Progress', 'in-progress'
    FINISHING = 'Finishing', 'finishing'
    COMPLETED = 'Completed', 'completed'
    ABANDONED = 'Abandoned', 'abandoned'
    HALTED = 'Halted', 'halted'
    FROZEN = 'Frozen', 'frozen'

@unique
class PartnershipType(models.TextChoices):
    COLLABORATION = 'Collaboration', 'Collaborate with us'
    DEMO_REQUEST = 'Demo Request', 'Request for a demo'
    HIRE_US = 'Hire Us', 'Hire our services'

class ProjectState(models.Model):
    stage_name = models.CharField(max_length=64, blank=False)
    project_status = models.CharField(max_length=64, choices=ProjectStatus.choices, default=ProjectStatus.STARTING)
    start_date = models.DateField(auto_now_add=True)
    end_state = models.DateField(default=add_time(6))
    comment = models.TextField(max_length=324)

    def __str__(self):
        return self.stage_name + " - " + self.project_status

class ContactPerson(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    middle_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=False)
    job_function = models.CharField(max_length=128, blank=False)

    @property
    def full_name(self):
        return full_name(self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return self.full_name() + " - " + self.job_function


class Partner(models.Model):
    organisation_name = models.CharField(max_length=128, blank=False)
    contact_email = models.EmailField(unique=True, blank=False)
    partnership_type = models.CharField(max_length=64, choices=PartnershipType.choices, default=None)
    project_status = models.CharField(max_length=64, choices=ProjectStatus.choices, default=ProjectStatus.STARTING)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.organisation_name

