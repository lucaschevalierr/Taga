from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.


def login(request):

    return render(request, "user/login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('notation-index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            user = User.objects.get(username='')
            user.username = user.email
            user.save()

            return redirect('user-login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, "user/register.html", context)
