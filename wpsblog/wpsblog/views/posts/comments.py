from django.shortcuts import redirect

from wpsblog.models import Post


def comments_create(request, post_id):
    content = request.POST.get("content")
    post = Post.objectis.POST.get(id=post_id)
    comment = post.comment_set.create(
        content=content,
    )
    return redirect(comment)
