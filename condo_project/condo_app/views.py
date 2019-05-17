# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from django.urls import reverse_lazy
# from django.views import generic


# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def index(request):
    # return HttpResponse("Hello, you are in the main landing page")
    return render(request, 'landing_page/signup.html')
    
def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = SignUpForm()
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})