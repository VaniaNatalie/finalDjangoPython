from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm


# Signup form
def signup(request):
    # Signup form submission
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account created! Let's login!")
            return redirect('login')

    # If user already have an account
    elif request.user.is_authenticated:
        return redirect('app-home')
    else:
        form = SignUpForm
    return render(request, 'users/signup.html', {'form': form})