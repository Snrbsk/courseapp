from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from account.forms import LoginUserForm, CreateUserForm, ChangePasswordForm


def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request,"account/login.html",{"error" : "Insufficient authorization."})
    
    if request.method == "POST":
        form = LoginUserForm(request, data = request.POST)
        if form.is_valid():
            username =form.cleaned_data["username"]        
            password =form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                nextUrl = request.GET.get("next", None)

                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else :
                return render(request, "account/login.html", {"form":form})
        else :
            return render(request, "account/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render(request, "account/login.html", {"form":form})

def user_register(request):
    if request.method=="POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username = username, password = password)
            login(request,user)
            return redirect("index")
        else:
            return render(request, "account/register.html", {"form":form})
    else:
        form = CreateUserForm()
        return render(request, "account/register.html", {"form":form})
       
def user_logout(request):
    logout(request)
    return redirect("index")

def change_password(request):
    if request.method =="POST":
        form = ChangePasswordForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            user_logout
            return redirect("user_login")
        else:
            return render(request,"account/changePassword.html", {"form":form})

    else:
        form = ChangePasswordForm(request.user)
    return render(request,"account/changePassword.html", {"form":form})

 