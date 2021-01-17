from django.contrib import admin

from note.models import Note, NoteImage

# Register your models here.

admin.site.register(Note)


admin.site.register(NoteImage)
