from django.contrib.auth.models import User
from django.shortcuts import render

from app.models.Pet import Pet


def my_posts_view(request, username):
    user = User.objects.get(username=username)
    pets = Pet.objects.filter(user=user)
    try:
        pet_user = pets[0].user.username
    except:
        pet_user = username
    context = {
        'Pets': pets,
        'pet_user': pet_user
    }
    return render(request, 'my_posts_page.html', context)
