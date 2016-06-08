from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as suth_login

def login(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        passwod = request.POST.get("password")
        user = User.objects.create_user(
            username=username,
            password=password,
        )

    if user:
        auth_login(request, user)
        return redirect(reverse("home"))
