from csk.views import *

from django.urls import path

app_name='csk'

urlpatterns=[

    path('rohit/',rohit,name='rohit'),
    path('msd/',msd,name='msd'),
]