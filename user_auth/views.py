import io
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import authenticate, login
from .models import Profile

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()


			# user_profile = Profile.objects.get(user=user)
			# user_profile.is_user = True
			# user_profile.save()

			Profile.objects.create(user= user)

			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("app:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="user_auth/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("app:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="user_auth/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("user_auth:login")
    