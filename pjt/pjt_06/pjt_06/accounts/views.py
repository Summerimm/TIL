from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {'form': form,}
    return render(request, 'accounts/update.html', context)


@require_http_methods(['GET', 'POST'])
def change_password(request):
    if not request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)

    context = {'form': form,}
    return render(request, 'accounts/change_password.html', context)

@require_safe
def profile(request, username):
    person = get_user_model().objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, username):
    if request.user.is_authenticated:
        person = get_user_model().objects.get(username=username)
        print(person)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')