from django.shortcuts import render


def detail(request, posts_id):
    return render(
        request,
        "posts/detail.html",
        {},
    )
