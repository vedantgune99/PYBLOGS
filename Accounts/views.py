from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from Accounts.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os

# Create your views here.


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
            return redirect('/')

        else:
            messages.add_message(request, messages.ERROR,
                                 "Try Again, Wrong Credentials!")
            print("user successfully logged in!")

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged out successfully!")
    return redirect('/')


def user_signin(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if (pass1 == pass2):
            profile = Profile()
            user = User.objects.create_user(first_name=fname, last_name=lname,
                                            username=username, email=email, password=pass1)

            profile.user = user
            profile.phone = phone
            profile.save()
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "User signed in successfully!")
            return redirect('/accounts/login')
        else:
            messages.add_message(request, messages.ERROR,
                                 "There was an error, Try again!")

    return render(request, 'signin.html')


def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


def del_profile_img(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.profile_pic = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp"
    user.profile.save()
    return redirect('/')


def edit_profile(request, user_id):
    pobjs = Profile.objects.filter(user=user_id)

    if request.method == 'POST':
        if request.FILES:
            doc = request.FILES  # returns a dict-like object
            doc_name = doc['image']

        # profile_image = request.FILES['image']
        username = request.POST['username']
        phone = request.POST['phone']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        user = User.objects.get(username=username)
        user.first_name = fname
        user.last_name = lname
        user.email = email

        user.profile.user = request.user
        user.profile.phone = phone

        if not (request.FILES):
            if ('/media/' in user.profile.profile_pic):
                user.profile.profile_pic = "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp"
        else:
            user.profile.profile_pic = doc_name

        user.profile.save()
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             'Profile updated successfully!')

    return render(request, 'edit_profile.html', {'pobjs': pobjs, 'user': request.user})
