from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .base import PostBaseView

from wpsblog.models import Post


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        return queryset.filter(is_public=True)
# def list(request):
#     page = request.GET.get("page", 1)
#     per = request.GET.get("per", 5)
#     paginator = Paginator(Post.objects.public(), per)
#     posts = paginator.page(page)
#     return render(
#         request,
#         "posts/list.html",
#         {
#             # "posts": Post.objects.public(),
#             "posts": posts,
#         },
#     )
#     page = request.GET.get("page", 1)
#     per = request.GET.get("page", 5)
#     paginator = Pagi
#     class PostListView(ListView):
#     model = Post
#     templete_name = "posts/list.html"
#     context_object_name = "posts"
