from django.shortcuts import render, redirect
from user_profile.forms import RegisterForm
from django.contrib.auth.models import User
from user_profile.models import UserProfile

def profile(request):
    user_profile = request.user.get_profile()
    return render(request, 'profile.html', {'user_profile':user_profile, })

def register(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            save_form(form)
            return redirect('/')
    return render(request, 'register.html', {'form': form, })

def save_form(form):
    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
    UserProfile.objects.create(user=user, address=form.cleaned_data['address'], phone_number=form.cleaned_data['phone_number'])
