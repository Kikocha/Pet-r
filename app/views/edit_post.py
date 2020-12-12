from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms.pet_form import PetForm
from app.models.Pet import Pet


@login_required
def edit_post(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
    except:
        return render(request, 'pet_not_exists.html')
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet
        }
        return render(request, 'edit_post.html', context)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': form,
            'pet': pet
        }
        return render(request, 'edit_post.html', context)
