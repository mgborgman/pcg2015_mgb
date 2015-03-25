from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "BOLD BOLD BOLD"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'pagename': "about"}
    return render(request, 'rango/about.html', context_dict)


def contact(request):
    context_dict = {'email': "mgborgman@gmail.com"}
    return render(request, 'rango/contact.html', context_dict)


