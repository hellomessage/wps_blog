from django.views.generic.list import ListView

from django.shortcuts import render
from django.core.paginator import Paginator

from wpsblog.models import Post


def list(request):
#    page = request.GET.get("page", 1)
#    per = request.GET.get("page", 5)
#
#    paginator = Pagi
    return render(
        request,
        "posts/list.html",
        {
            "posts": Post.objects.public(),
        },
    )
'''
#class PostListView(ListView):
#    model = Post
#    templete_name = "posts/list.html"
#    context_object_name = "posts"
##from django.shortcuts import render
#
#from wpsblog.models import Post
'''
