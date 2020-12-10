from django.shortcuts import render

from app.models.Pet import Pet


def home_page(request):
    context = {
        'Pets': Pet.objects.all()
    }
    return render(request, 'home_page.html', context)
