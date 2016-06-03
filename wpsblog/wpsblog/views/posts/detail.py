from django.shortcuts import render

from wpsblog.models import Post


def detail(request, posts_id):
    return render(
        request,
        "posts/detail.html",
        {
            "post": Post.objects.get(id=posts_id)
        },
    )
