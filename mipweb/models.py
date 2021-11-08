from django.db import models
from enum import Enum, auto, unique
from strenum import StrEnum
from django.db.models.deletion import CASCADE

from django.db.models.fields import EmailField
from .utils import full_name


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


class ContactPerson(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = EmailField()
    function_role = models.CharField(max_length=128)

    @property
    def full_name(self):
        "Returns the contact person's full name."
        return full_name(self.first_name, self.last_name, self.middle_name)

    def __str__(self) -> str:
        return full_name(self)


class Partnership(models.Model):

    @unique
    class PartnershipType(StrEnum):
        DEMO_REQUEST = 'Request for Demo'                 #PartnershipType.DEMO_REQUEST.label = 'Demo Request'
        DONATE_TO_PROJECT = 'Donate to Project'
        HIRE_SERVICE = 'Hire our Services'
        RESEARCH_COLLABO = 'Collaborate with us'

    name = models.CharField(max_length=128)
    description = PartnershipType.DEMO_REQUEST
    partnership_domain = models.ManyToManyField(PartnershipArea)

    def __str__(self) -> str:
        return self.name + " - " + self.description


class Partner(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    partnerships = models.ManyToManyField(Partnership)

    def __str__(self) -> str:
        return self.name


class Donor(models.Model):
    organisation_name = models.CharField(max_length=64)
    amount_pledged = models.DecimalField(max_digits=7, decimal_places=2)
    contact_person_first_name = models.CharField(max_length=128)
    contact_person_middle_name = models.CharField(max_length=128)
    contact_person_last_name = models.CharField(max_length=128)
    contact_person_email = EmailField()
    contact_person_function_role = models.CharField(max_length=128)

    @property
    def full_name(self):
        "Returns the contact person's full name."
        return full_name(self.contact_person_first_name, 
                         self.contact_person_last_name, 
                         self.contact_person_middle_name)

    def __str__(self) -> str:
        return full_name(self)
