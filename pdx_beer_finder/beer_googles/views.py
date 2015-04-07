from django.shortcuts import render
from models import Bar

# Create your views here.
def index(request):
    bars = Bar.objects.all()

    context_dict = {'bar': bars}
    return render(request, 'index.html', context_dict)