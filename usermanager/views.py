from django.shortcuts import render, redirect

from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect("/register")
        return redirect("/home")
    else:
        form = RegisterForm()
    
    return render(response, "usermanager/register.html", {"form": form})
