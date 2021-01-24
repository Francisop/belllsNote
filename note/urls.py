from os import name
from django.urls import path
from note.views import (AboutUs, Index, NoteView, PrintView)

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('note/',NoteView.as_view(), name='note'),
    path('print/',PrintView.as_view(), name='print'),
    path('about-us/',AboutUs.as_view(), name='about-us')
]
