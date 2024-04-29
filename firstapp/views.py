from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib import messages


# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account created successfully")
                form.save(commit=True)
        else:
            form = RegisterForm()
        return render(request, "firstapp/signup.html", {"form": form})
    else:
        return redirect("profile")


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, "firstapp/login.html", {"form": form})
    else:
        return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "Profile edited successfully")
                form.save()
        else:
            form = ChangeProfileForm(instance=request.user)
        return render(
            request, "firstapp/profile.html", {"user": request.user, "form": form}
        )
    else:
        return redirect("login")


def logout_user(request):
    logout(request)
    return redirect("login")


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "firstapp/change_pass.html", {"form": form})
    else:
        return redirect("login")


def change_pass2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "firstapp/change_pass2.html", {"form": form})
    else:
        return redirect("login")
