from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'pagename': "about"}
    return render(request, 'rango/about.html', context_dict)


def contact(request):
    context_dict = {'email': "mgborgman@gmail.com"}
    return render(request, 'rango/contact.html', context_dict)


def category(request):
    context_dict = {}

    try:
        Category.Objects.get(slug = category_name_slug)
        context_dict['category_name'] = category.name
        


