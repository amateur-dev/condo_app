from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .models import Facility
from .models import Condo


def index(request):
    context = {
    }
    if request.user.is_authenticated:
        user = request.user
        context = {
            "facilities": Facility.objects.filter(condo__name=user.condo_name),
        }
    # return HttpResponse("Hello, you are in the main landing page")
    return render(request, 'landing_page/index.html', context)


def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Condo.objects.create(name=form.condo_name)
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mainLandingPage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def facility(request, facility):
    return HttpResponse(f"Hello, you are in the facility booking page of {facility}")
