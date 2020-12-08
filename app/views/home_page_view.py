from django.shortcuts import render

from app.models.Pet import Pet


def home_page(request, version='all'):
    if version == 'all':
        context = {
            'Pets': Pet.objects.all()
        }
    else:
        pets = Pet.objects.get(type=version)
        context = {
            'Pets': pets
        }
    return render(request, 'home_page.html', context)
