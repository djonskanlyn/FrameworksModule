from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #Added import here
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully, now you can login.')
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required # Added decorator here
def profile(request): 
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')