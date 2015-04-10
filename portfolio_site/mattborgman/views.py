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


def about(request):
    context_dict = {}
    return render(request, 'about.html', context_dict)


