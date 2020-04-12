from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Create your views here.

# def signup(request):
#     obj = SignUPTable.objects.get(id=1)
#
#     context = {
#         "data": "obj"
#     }
#
#     return render(request, 'user/signup.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Your account created successfully {username}')
            login(request, user)
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')

# def login(request):
#     obj = SignUPTable.objects.get(id=1)
#
#     context = {
#         "data": "obj"
#     }
#
#     return render(request, 'user/login.html', context)
