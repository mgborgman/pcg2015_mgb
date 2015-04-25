from django.shortcuts import render, redirect
from models import Bar, Beer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json

# Create your views here.

def index(request):
    bar_list = Bar.objects.all()
    beer_list = Beer.objects.all()
    bar_results = None
    beer_results = None
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    if 'bar_submit' in request.POST:

        query = request.POST['bar_search']
        bar_results = Bar.objects.filter(name__contains=query)


    elif 'beer_submit' in request.POST:

        query2 = request.POST['beer_search']
        beer_results = Beer.objects.filter(name__contains=query2)

    context_dict = {'bar_results': bar_results, 'beer_results': beer_results, 'bar_list': bar_list, 'beer_list': beer_list, 'username': username}
    return render(request, 'index.html', context_dict)


def welcome(request):
    context_dict = {}
    return render(request, 'welcome.html', context_dict)


def register(request):


    user_list = list(User.objects.all().values_list('username', flat=True))



    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verify_password = request.POST['verify_password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('success')

    context_dict = {'user_list': json.dumps(user_list)}
    return render(request, 'register.html', context_dict)


def signin(request):
    disabled_account = "disabled account"
    failed_login = "failed login"

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                disabled_account
        else:
            failed_login

    context_dict = {}
    return render(request, 'sign_in.html', context_dict)


def success(request):
    context_dict = {}

    return render(request, 'success.html', context_dict)


def bar_data(request):
    data = {'name': Bar.name, 'beer': Bar.beers, 'description': Bar.description}
    json_bar_data = json.dumps(data)
