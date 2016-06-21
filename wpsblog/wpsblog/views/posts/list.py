from django.views.generic import ListView
from django.core.paginator import Paginator
from .base import PostBaseView

from wpsblog.models import Post


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_paginate_by(self, queryset):
        return self.request.GET.get("per", 5)
    # 1. get_context_data
    # 2. get_queryset
    # 3. ListView, get_paginate_by
# ###########################################################
#     def get_queryset(self):
#         # context 중에서 object_list로 들어갈 queryset
#         queryset = super(PostListView, self).get_queryset()
#         page = self.request.GET.get("page", 1)
#         per = self.request.GET.get("per", 5)
#         paginator = Paginator(queryset, per)
#         paginator = Paginator(queryset.filter(is_public=True), per)
#         return paginator.page(page)
# ###########################################################
#         queryset = super(PostListView, self).get_queryset()
#         return queryset.filter(is_public=True)
# ###########################################################
#     def get_context_data(self, **kwargs):
#         # context_date를 전달하는 함수
#         context = super(PostBaseView, self).get_context_data(**kwargs)
#         page = self.request.GET.get("page", 1)
#         per = self.request.GET.get("per", 5)
#         paginator = Paginator(context[self.context_object_name ],  per)
#         context[self.context_object_name] = paginator.page(page)
#         return context
# ###########################################################
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
# ###########################################################
#     page = request.GET.get("page", 1)
#     per = request.GET.get("page", 5)
#     class PostListView(ListView):
#     model = Post
#     templete_name = "posts/list.html"
#     context_object_name = "posts"
