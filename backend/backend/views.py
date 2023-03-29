from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from backend.forms import UserPasswordChangeForm


def home_view(request):
    data = Some.objects.all()
    context = {
        'data': data
    }
    return render(request, 'user/home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message.success(request, f"Successfully logged in as {username}")
            return redirect("home:user")
        else:
            message.error(request, f"Username and password not found for the {username}")
            return redirect("home:login")

def logout_view(request):
    logout(request)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = User.objects.get(username=username)
            if user is not None:
                message.error(request, f"User with {username} already exist")
                return redirect("home:register")
            else:
                message.success(request, f"User registerd successfully")
                return redirect("home:login")
    context = {}
    return render(request, "user/register.html", context)

def user_view(request):
    if not request.user.is_authenticated:
        return render(request, 'user/main.html')
    username = request.user.username
    user = User.objects.get(username)
    form = UserUpdateForm(request.POST or None, instance=User)
    confirm = False
    if form.is_valid():
        form.save()
        confirm = True
    context = {
        'user': user,
        'form': form
    }
    return render(request, 'user/home.html', context)

def change_password_view(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            userinstance = form.save(commit=False)
            userinstance.set_password(userinstance.cleaned_data.get("password"))
            form.save(commit=True)
            message.success(request, "Successfully updated user password")
            return redirect(request, "home:user")
        else:
            message.error(request, "User not authenticated")
            return redirect(request, "home:view")
    form = UserPasswordChangeForm()
    return render(request, "user/change_password.html", context={"form": form})
