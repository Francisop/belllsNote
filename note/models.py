from django.db import models
from django.db.models.enums import Choices

# Create your models here.

DELIVERY_LOCATION_CHOICES = [
    ('HD', 'Hall D'),
    ('ELT', 'Edozian lecture THeatre'),
    ('Coleng', 'College of Engineering'),
    ('Colenv', 'College of Environmental Science'),
    ('Colmas', 'College of Mangement Science'),
    ('Colnas', 'College of Natural Science'),
    ('Bronze male hostel', 'Bronze male hostel'),
    ('Bronze female hostel', 'Bronze female hostel'),
    ('Silver female hostel', 'Silver female hostel'),
    ('Silver 1 male hostel', 'Silver 1 male hostel'),
    ('Silver 2 male hostel', 'Silver 2 male hostel'),
    ('Silver 3 male hostel', 'Silver 3 male hostel'),
    ('marque', 'Marque'),
    ('hall b', 'Hall B')
]


class Note(models.Model):
    delivery_location = models.CharField(
        max_length=100, choices=DELIVERY_LOCATION_CHOICES)
    mobile_number = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    deadline = models.DateField()  # auto_now_add=True

    def __str__(self):
        return self.name


class NoteImage(models.Model):
    image = models.ImageField(upload_to='images/')
    note = models.ForeignKey(Note, on_delete=models.CASCADE)


    def __str__(self):
        return self.note.name
