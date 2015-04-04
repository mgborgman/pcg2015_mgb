from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': 'TEST'}
    return render(request, 'index.html', context_dict)



