from note.models import Note, NoteImage
from django import forms
from django.forms import ModelForm, widgets


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['delivery_location', 'mobile_number', 'name', 'deadline']


class NoteImageForm(ModelForm):
    class Meta:
        model = NoteImage
        fields = ['image']
        widgets = {
            'image': widgets.FileInput(attrs={'multiple': ''}),
        }
