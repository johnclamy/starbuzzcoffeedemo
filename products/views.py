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
        'price': 1495.00,
        'image_url': 'https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2F2YXBvb3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60'
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
        'price': 1400,
        'image_url': 'https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHVsZ3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60'
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
        'price': 299.99,
        'image_url': 'https://images.unsplash.com/photo-1517423440428-a5a00ad493e8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YW5hdG9saWFuJTIwU2V0dGluZ2VyfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60'
    }
]


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Pets-R-Us | Products page',
        'products': products,
    }

    return render(request, 'products/index.html', context)
