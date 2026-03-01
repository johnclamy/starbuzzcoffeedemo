from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'default/index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'default/about.html')
