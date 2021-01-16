from note.models import Note, NoteImage
from django.shortcuts import render
from django.views import View
from note.forms import NoteForm, NoteImageForm

# Create your views here.



class Index(View):
    template_name = 'index.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)




class NoteView(View):
    note_form_class = NoteForm
    note_image_form_class = NoteImageForm
    template_name = 'note_test.html'

    def get(self, request, *args, **kwargs):
        noteForm = self.note_form_class
        noteForm2 = self.note_image_form_class
        return render(request, self.template_name, {'note_form': noteForm, 'note_form2': noteForm2})


    def post(self, request, *args, **kwargs):
        noteForm = self.note_form_class(request.POST)
        noteForm2 = self.note_image_form_class(request.POST, request.FILES)
        file = request.FILES.getlist('image')

        if noteForm.is_valid() and noteForm2.is_valid():
            name = noteForm.cleaned_data['name']
            delivery_location = noteForm.cleaned_data['delivery_location']
            mobile_number = noteForm.cleaned_data['mobile_number']
            deadline = noteForm.cleaned_data['deadline']
            note = Note(name=name,
                        delivery_location=delivery_location, mobile_number=mobile_number,deadline=deadline)
            note.save()
            # work on the multiple images first
            if file:
                for img in file:
                    print(img)
                    NoteImage.objects.create(image=img, note=Note.objects.get(id = note.pk))

        return render(request, 'thank_you.html', {})




def thank_you_view(request):
    return render(request,'thank_you.html',{})

