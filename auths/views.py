from django.shortcuts import render, redirect
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Account
from django.contrib import messages


# Create your views here.

#REGISTER VIEW
def registerView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated: 
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            print(account)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            if account.profile_updated:
                messages.success(request, f"{account.username} Registered Successfully")
                return redirect('index')
            else:
                messages.success(request, f"{account.username}, you need to update your account")
                return redirect('update_user')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'auth/register.html', context)


#LOGIN VIEW
def loginView(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                destination = get_redirect_if_exist(request)
                if destination:
                    return redirect(destination)
                if user.profile_updated:
                    messages.info(request, f"Login Successfully")
                    return redirect("index")
                else:
                    messages.info(request, f"Login Successfully")
                    return redirect('update-user')
				
        else:
            form = AccountAuthenticationForm()
            context['login_form'] = form
    return render(request, 'auth/login.html', context)

def get_redirect_if_exist(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get('next'))
    return redirect

#LOGOUT VIEW
def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

def update_profile(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES, instance = request.user)
        print(form)
        if form.is_valid():
            upd = form.save()
            print(upd)
            upd.profile_updated = True
            upd.save()
            return redirect("index")
    else:
        form = AccountUpdateForm()
        context['form'] = form 
    #context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
    return render(request, 'auth/update_profile.html', context)




