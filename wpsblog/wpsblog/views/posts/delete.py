from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from wpsblog.models import Post


def delete(request, post_id):
    print(post_id)
    post = Post.objects.get(id=post_id)
    print(post)
    post.delete()

    return redirect(
        reverse("posts:list"),
    )
