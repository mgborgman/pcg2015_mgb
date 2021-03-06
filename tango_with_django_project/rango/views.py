from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    category_most_views_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'views': category_most_views_list}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'pagename': "about"}
    return render(request, 'rango/about.html', context_dict)


def contact(request):
    context_dict = {'email': "mgborgman@gmail.com"}
    return render(request, 'rango/contact.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug = category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})
        


