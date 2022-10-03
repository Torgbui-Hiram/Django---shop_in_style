from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from . forms import RegisteredUserForm


# Register member
def register_user(request):
    if request.method == "POST":
        form = RegisteredUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful')
            return HttpResponseRedirect('/')
    else:
        form = RegisteredUserForm()
    return render(request, 'register/user_register.html', {'form': form, })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            messages.success(
                request, 'Sorry! There Was Aan Error Logging In. Try Again')
            return redirect('user-login')

    else:
        return render(request, 'register/user_login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out succesfully')
    return redirect('/')
