from django.views.generic.edit import CreateView

from .base import PostBaseView


class PostCreateView(PostBaseView, CreateView):
    fields = [
        "title",
        "content",
        "image",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
    # title
    # content
    # image
    # user

#     def post(self, request, *args, **kwargs):
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         image = request.FILES.get("image")
#         post = Post.objects.create(
#             user=request.user,
#             title=title,
#             content=content,
#             image=image,
#         )
#         return redirect(post)
