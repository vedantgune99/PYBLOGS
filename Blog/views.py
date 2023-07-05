from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'base.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if (user is not None):
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 "Logged in Successfully!")
            print("User Logged in Successfully!")

        else:
            messages.add_message(request, messages.ERROR,
                                 "Try Again, Wrong Credentials!")
            print("user successfully logged in!")
            return redirect('/login')

    return render(request, 'login.html')


def user_signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if (pass1 == pass2):
            user = User.objects.create_user(
                username=username, email=email, password=pass1)
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "User signed in successfully!")
        else:
            messages.add_message(request, messages.ERROR,
                                 "There was an error, Try again!")

    return render(request, 'signin.html')


def forgot_pass(request):
    pass


def about(reqeust):
    pass


def contact(reqeust):
    pass
