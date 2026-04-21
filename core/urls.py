from django.urls import path
from .views import index, about


urlpatterns = [
    path('', index, name='core.index'),
    path('about', about, name='core.about'),
]

