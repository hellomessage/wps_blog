from django.shortcuts import render

from wpsblog.models import Post


def new(request, post_id):
    return render(
        request,
        "posts/new.html",
        {}
    )
