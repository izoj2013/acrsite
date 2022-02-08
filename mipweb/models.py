from django.db import models
from enum import Enum, auto, unique
from strenum import StrEnum
from django.db.models.deletion import CASCADE

from django.db.models.fields import EmailField
from .utils import full_name

@unique
class PartnershipType(StrEnum):
    DEMO_REQUEST = 'Request for Demo'                 #PartnershipType.DEMO_REQUEST.label = 'Demo Request'
    DONATE_TO_PROJECT = 'Donate to Project'
    HIRE_SERVICE = 'Hire our Services'
    RESEARCH_COLLABO = 'Collaborate with us'

@unique
class ExpertiseType(StrEnum):
    CENTRE_EXCELLENCY = 'Centre of Excellency'
    CONSULTANCY = 'Concultancy'
    INVENTION = 'Invention'
    RESEARCH = 'Research'
    TRAINING = 'Training'

@unique
class ExpertStrength(Enum):
    INDIVIDUAL = auto()
    GROUP = auto()


class TeamMember(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    #picture = models.ImageField(upload_to='images')
    member_bio = models.TextField()

    @property
    def full_name(self):
        "Returns the Team Member's full name."
        return full_name(self.first_name, self.last_name, self.middle_name)

    def __str__(self) -> str:
        return self.full_name(self)


class Expertise(models.Model):
    name = models.CharField(max_length=128)
    expertise_type = ExpertiseType.INVENTION
    expertise_strength = ExpertStrength.GROUP

    def __str__(self):
        return self.name;


class PartnershipArea(models.Model):

    name = models.CharField(max_length=128)
    expertise = models.ManyToManyField(Expertise)

    def __str__(self) -> str:
        return self.name