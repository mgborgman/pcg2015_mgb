from django.shortcuts import render
from models import Bar, Beer


# Create your views here.

def index(request):
    beer_results = None
    bar_results = None
    if request.POST:

        query = request.POST['bar_search']
        bar_results = Bar.objects.filter(name__contains=query)

        query2 = request.POST['beer_search']
        beer_results = Beer.objects.filter(name__contains=query2)










    context_dict = {'bar_results': bar_results, 'beer_results': beer_results}
    return render(request, 'index.html', context_dict)