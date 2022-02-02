from django.db import models
from django.urls import reverse

from mipweb.utils import full_name

# Create your models here.

class Donor(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    organisation = models.CharField(max_length=128)
    registration_date = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        "Returns the Team Member's full name."
        return full_name(self.first_name, self.last_name, self.middle_name)

    def __str__(self) -> str:
        return self.full_name()

    def get_absolute_url(self):
        return reverse('mip-donor-detail', kwargs={'pk': self.pk})
