from django import forms
from django.forms import ModelForm, widgets
from note.models import Note, NoteImage
# from multiupload import


class NoteForm(ModelForm):
    class Meta:
        # note_pic = MyFormField(min_num=1, max_num=3, max_file_size=1024*1024*5)
        model = Note
        fields = ['delivery_location', 'mobile_number', 'name', 'deadline']


class NoteImageForm(ModelForm):
    def __ini__(self, *args, **kwargs):
        self.fields['image'].widget.attrs = {'attribute': 'multiple'}

    class Meta:
        model = NoteImage
        fields = ['image']
        widgets = {
            'image': widgets.FileInput(attrs={'multiple': ''}),
        }
