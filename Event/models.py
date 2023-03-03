from django.db import models
from django.core.exceptions import ValidationError
import datetime
from Person.models import Person

# Create your models here.
def is_date_valid(value):
    if value < datetime.date.today():raise ValidationError('date ne doit pas etre au passé!!!!!!  ')



class Event(models.Model):
    title = models.CharField("Title",default="",max_length=250)
    description = models.TextField()
    state = models.BooleanField(default=False)
    imageEvent=models.ImageField(upload_to='images/',blank=True)
    nbParticipants = models.IntegerField(default=0)
    CATEGORY_CHOICES = ( ('music','Music'), ('sport','Sport'), ('cinema','Cinema') )
    category = models.CharField(max_length=10 , choices=CATEGORY_CHOICES)
    dateEvent = models.DateField(validators=[is_date_valid])
    createdAt =models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    organizer = models.ForeignKey(Person, on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        Person,
        related_name = "participations",
        through="Participation"
    )
    def __str__(self):
       return self.title
       



class Participation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event= models.ForeignKey(Event, on_delete=models.CASCADE)
    datePart= models.DateField(auto_now=True)
    class Meta:
        unique_together =('person','event')
        verbose_name_plural = 'Participations'