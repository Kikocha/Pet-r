from django.shortcuts import render

from app.models.Pet import Pet
from app.models.extend_user import ExtendUser


def details_post(request, pk):
    pet = Pet.objects.get(pk=pk)
    user = pet.user
    try:
        extend_user = ExtendUser.objects.get(user=user)
    except:
        extend_user = False
    context = {
        'pet': pet,
        'extend_user': extend_user
    }
    return render(request, 'details_post.html', context)
