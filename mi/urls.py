from mi.views import *

from django.urls import path

app_name='mi'

urlpatterns=[

    path('arjun/',arjun,name='arjun'),
    path('bumrah/',Bumrah,name='bumrah'),
]