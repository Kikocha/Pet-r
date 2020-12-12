from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app.models.Pet import Pet


@login_required
def delete_post(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except:
        return render(request, 'pet_not_exists.html')
    if request.user.username != pet.user.username:
        return render(request, 'delete_if_invalid_user.html')
    pet.delete()
    return redirect('home page')
