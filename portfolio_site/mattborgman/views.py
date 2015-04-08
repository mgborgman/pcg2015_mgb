from django.shortcuts import render
from django.views import generic
from . import models


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog_home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"


def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)

def test(request):
    context_dict = {}
    return render(request, 'test.html', context_dict)

