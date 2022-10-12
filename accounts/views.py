from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginpage(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Logged in successfully!!!')
            return redirect('index')
        else:
            messages.info(request, 'username or password incorrect!!!')
            return redirect('loginpage')
    else:
        return render(request, "accounts/loginpage.html")


def logout(request):
    auth.logout(request)
    messages.info(request, 'logged out')
    return redirect('index')


def accounts(request):

    if request.method == 'POST':

        email = request.POST['email'].lower()
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username'].lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:

            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():

                #print('username or email already taken')
                messages.info(request, 'username or email already taken')
                return redirect('accounts')

            else:

                user = User.objects.create_user(email=email, first_name=firstname,last_name=lastname,password=password1,username=username)
                user.save()

                new_user = auth.authenticate(username=username, password=password1)
                auth.login(request, new_user)

                messages.info(request, 'user created and logged in')
                #print('user created')
                return redirect('index')
        else:

            #print('check password!!')
            messages.info(request, 'check password!!')
            return redirect('accounts')

    else:

        return render(request, "accounts/accounts.html")


