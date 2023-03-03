from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
import datetime

# Create your models here.


def mail_esprit(mail):
   if str(mail).endswith('@esprit.tn') ==False: raise ValidationError('please check your email!!  ')


class Person(AbstractUser):
    email = models.EmailField("Email",unique=True, validators=[mail_esprit])
    cin = models.CharField("Cin",primary_key=True,max_length=8,validators=[MaxLengthValidator(8),MinLengthValidator(8)])
    createdAt =models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

