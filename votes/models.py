from django.db import models
from datetime import datetime

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return 'Position {}'.format(self.name)

class Candidate(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    birthdate = models.DateField(null=True, blank=True)
    platform = models.TextField()

    def __str__(self):
        return 'Candidate: {}'.format(self.firstname, self.lastname)

class Vote(models.Model):
    name = models.CharField(max_length = 100)
    candidate = models.ForeignKey(Candidate,
                on_delete = models.CASCADE,
                related_name = 'candidates',
                null=True, blank=True)
    vote_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return 'Position {}'.format(self.name)
