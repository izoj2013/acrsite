from django.db import models
from email.policy import default
from enum import unique
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField

from mipweb.utils import full_name

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
    COLLABORATION = 'Collaboration', 'collaboration'
    DEMO_REQUEST = 'Demo Request', 'demo request'
    HIRE_US = 'Hire Us', 'hire us'

class ProjectStage(models.Model):
    stage_name = models.CharField(max_length=64, blank=False)
    project_status = models.CharField(max_length=64, choices=ProjectStatus.choices, default=ProjectStatus.STARTING)
    start_date = models.DateField(editable=True)
    end_state = models.DateField(editable=True)
    comment = models.TextField(max_length=324)

    def __str__(self):
        return self.stage_name + ": " + self.project_status

class ContactPerson(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    middle_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=False)
    job_function = models.CharField(max_length=128, blank=False)

    @property
    def full_name(self):
        return full_name(self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return self.full_name() + "-" + self.job_function


class Partner(models.Model):
    organisation_name = models.CharField(max_length=128, blank=False)
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    partneship_type = models.CharField(max_length=64, choices=PartnershipType.choices, default=PartnershipType.DEMO_REQUEST)
    project_name = models.CharField(max_length=128, blank=False)
    project_stage = models.ForeignKey(ProjectStage, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name + "-" + self.partneship_type + "-" + self.organisation_name

