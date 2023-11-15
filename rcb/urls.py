from rcb.views import *

from django.urls import path

app_name='rcb'

urlpatterns=[

    path('virat/',virat,name='virat'),
    path('maxwell/',maxwell,name='maxwell'),
]