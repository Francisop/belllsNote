from os import name
from django.urls import path
from note.views import (Index)

urlpatterns = [
    path('',Index.as_view(), name='index'),
]
