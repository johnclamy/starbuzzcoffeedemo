from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Dummy data for products
products = [
    {
        'id': 1,
        'name': 'Reggie',
        'breed': 'Cavapoo',
        'gender': 'Male',
        'age_in_weeks': 13,
        'size': 'Small',
        'is_vaccinated': True,
        'descr': 'Apricot male puppy, playful and socialized. Parents are health tested and have great temperaments. Puppies come with a health guarantee.',
        'price': 1495.00
    },
    {
        'id': 2,
        'name': 'Unnamed',
        'breed': 'Pug',
        'gender': 'Female',
         'age_in_weeks': 9,
        'size': 'Small',
        'is_vaccinated': True,
        'descr': 'KC registered fawn pug puppies born in February, ready for new homes. Parents are health tested and have great temperaments. Puppies are socialized and come with a health guarantee.',
        'price': 1400
    },
    {
        'id': 3,
        'name': 'Dobby',
        'breed': 'Anatolian Shepherd',
        'gender': 'Male',
        'age_in_weeks': 28,
        'size': 'Large',
        'is_vaccinated': True,
        'descr': 'Gentle and loving neutered male, shy and requires patience to build confidence. He is good with other dogs and children. Dobby is looking for a patient and understanding home to thrive in.',
        'price': 299.99
    }
]


def product_list(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Pets-R-Us | Products page',
        'products': products,
    }

    return render(request, 'products/product-list.html', context)
