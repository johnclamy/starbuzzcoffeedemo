from django.urls import path
from views import *


urlpatterns = [
    path('', index, name='default_page.index'),
]
