from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


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
			return redirect('index')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'auth/register.html', context)


#LOGIN VIEW
def loginView(request):
    return render(request, 'auth/login.html')

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")

def update_profile(request):
    return render(request, 'auth/update_profile.html')


