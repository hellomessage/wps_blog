from django.views.generic.detail import DetailView

from wpsblog.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
# def detail(request, post_id):
#     return render(
#         request,
#         "posts/detail.html",
#         {
#             "post": Post.objects.get(id=post_id),
#         },
#     )
# from django.views.generic.list import ListView
# from .base import PostBaseView
# def PostDetailView(PostBaseView, ListView):
#     pass
# #    template_name = "posts/detail.html"
#     context_object_name = "posts"
#     return render(
#         request,
#         "posts/detail.html",
#         {
#             "post": Post.objects.get(id=post_id),
#         },
#     )
