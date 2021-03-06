from django.shortcuts import render, redirect
from models import Bar, Beer, BarRating
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.

def index(request):
    bar_list = Bar.objects.all()
    beer_list = Beer.objects.all()
    bar_rating = BarRating.objects.all()
    bar_results = None
    beer_results = None
    username = None
    if request.user.is_authenticated():
        username = request.user
    if 'bar_submit' in request.POST:

        query = request.POST['bar_search']
        bar_results = Bar.objects.filter(name__contains=query)


    elif 'beer_submit' in request.POST:

        query2 = request.POST['beer_search']
        beer_results = Beer.objects.filter(name__contains=query2)

    context_dict = {'bar_results': bar_results, 'beer_results': beer_results, 'bar_list': bar_list, 'beer_list': beer_list, 'username': username, 'bar_rating': bar_rating}
    return render(request, 'index.html', context_dict)


def welcome(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    context_dict = {'user':user}
    return render(request, 'welcome.html', context_dict)


def register(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
    user_list = list(User.objects.all().values_list('username', flat=True))



    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        verify_password = request.POST['verify_password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('success')

    context_dict = {'user_list': json.dumps(user_list), 'user':user}
    return render(request, 'register.html', context_dict)


def signin(request):
    user = None
    if request.user.is_authenticated():
        user = request.user
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

    context_dict = {'user':user}
    return render(request, 'sign_in.html', context_dict)


def success(request):
    context_dict = {}

    return render(request, 'success.html', context_dict)


# def bar_data(request):
#     data = {'name': Bar.name, 'beer': Bar.beers, 'description': Bar.description}
#     json_bar_data = json.dumps(data)

def bars(request, bar_slug):
    context_dict = {}

    try:
        bar = Bar.objects.get(slug = bar_slug)
        context_dict['bar_name'] = bar.name

        beers = Beer.objects.filter(bars = bar)
        context_dict['beers'] = beers
        context_dict['bar'] = bar
    except Bar.DoesNotExist:
        pass

    return render(request, 'bars.html', context_dict)

def beers(request, beer_slug):
    user = None
    if request.user.is_authenticated():
        user = request.user
    context_dict = {'user':user}

    try:
        beer = Beer.objects.get(slug = beer_slug)
        context_dict['beer_name'] = beer.name
        context_dict['beer'] = beer

    except Beer.DoesNotExist:
        pass

    return render(request, 'beers.html', context_dict)


def logout_view(request):
    logout(request)
    return redirect('signin')

