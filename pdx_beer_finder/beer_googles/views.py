from django.shortcuts import render
from models import Bar, Beer


# Create your views here.

def index(request):
    bar_list = Bar.objects.all()
    beer_list = Beer.objects.all()
    bar_results = None
    beer_results = None
    if 'bar_submit' in request.POST:

        query = request.POST['bar_search']
        bar_results = Bar.objects.filter(name__contains=query)


    elif 'beer_submit' in request.POST:

        query2 = request.POST['beer_search']
        beer_results = Beer.objects.filter(name__contains=query2)

    context_dict = {'bar_results': bar_results, 'beer_results': beer_results, 'bar_list': bar_list, 'beer_list': beer_list}
    return render(request, 'index.html', context_dict)


def welcome(request):
    context_dict = {}
    return render(request, 'welcome.html', context_dict)