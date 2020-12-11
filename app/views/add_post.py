from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.forms.pet_form import PetForm


@login_required
def add_post(request):
    if request.method == 'GET':
        context = {
            'form': PetForm,
        }
        return render(request, 'add_post.html', context)
    else:
        user_pk = int(request.POST['user'])
        user = User.objects.get(pk=user_pk)
        pet_form = PetForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.user = user
            pet.save()
            return redirect('home page')
        context = {
            'form': pet_form,
        }
        return render(request, 'add_post.html', context)
