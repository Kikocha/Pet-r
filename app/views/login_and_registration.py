from django.contrib.auth import login, logout, authenticate
from django.db import transaction
from django.shortcuts import render, redirect

from app.forms.login_form import LoginForm
from app.forms.registration_form import UserExtendForm, UserForm


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    if redirect_url:
        return redirect_url
    return 'home page'


def login_view(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm,
            'user_found': True
        }
        return render(request, 'registration_and_login/login.html', context)
    else:
        return_url = get_redirect_url(request.POST)
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(return_url)
        context = {
            'login_form': login_form,
            'user_found': False
        }
        return render(request, 'registration_and_login/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home page')


@transaction.atomic
def registration(request):
    if request.method == 'GET':
        context = {
            'user_form': UserForm,
            'user_extend_form': UserExtendForm
        }
        return render(request, 'registration_and_login/register.html', context)
    else:
        user = UserForm(request.POST)
        user_extend = UserExtendForm(request.POST)
        if user.is_valid() and user_extend.is_valid():
            profile = user.save()
            profile_extend = user_extend.save(commit=False)
            profile_extend.user = profile
            profile_extend.save()
            login(request, profile)
            return redirect('home page')
        context = {
            'user_form': user,
            'user_extend_form': user_extend
        }
        return render(request, 'registration_and_login/register.html', context)
