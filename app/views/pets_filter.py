from django.shortcuts import render

from app.models.Pet import Pet


def pets_filter(request, version):
    pets = [pet for pet in Pet.objects.all() if pet.type == version]
    context = {
        'Pets': pets,
        'type': version
    }
    return render(request, 'home_page.html', context)
