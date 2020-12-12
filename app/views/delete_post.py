from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app.models.Pet import Pet


@login_required
def delete_post(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.user.username != pet.user.username:
        return render(request, 'delete_if_user_dont_match.html')
    pet.delete()
    return redirect('home page')
