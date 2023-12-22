from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from products.models import Basket
from django.contrib.auth.decorators import login_required
# Create your views here


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST) # data from request variable
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html',context)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! You've successfully registered")
            return HttpResponseRedirect(reverse('users:login'))
    else:

        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/register.html',context)
@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:userprofile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance = request.user)




    context = {'title': 'Store - User Profile', 'form': form, 'basket': Basket.objects.filter(user=request.user)}
    return render(request, 'users/userprofile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))