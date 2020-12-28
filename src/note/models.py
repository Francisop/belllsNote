from django.db import models
from django.db.models.enums import Choices

# Create your models here.

DELIVERY_LOCATION_CHOICES = [
    ('HD', 'Hall D'),
    ('ELT', 'Edozian lecture THeatre'),
    ('Coleng', 'College of Engineering')
]


class Note(models.Model):
    delivery_location = models.CharField(
        max_length=10, choices=DELIVERY_LOCATION_CHOICES)
    mobile_number = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    deadline = models.DateTimeField(default='2012-09-04 06:00:00')  # auto_now_add=True

    def __str__(self):
        return self.name


class NoteImage(models.Model):
    image = models.ImageField(upload_to='images/')
    note = models.ForeignKey(Note, on_delete=models.CASCADE)


    def __str__(self):
        return self.note.name
