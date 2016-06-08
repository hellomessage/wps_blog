from django.shortcuts import render

from wpsblog.models import NaverPost


def naver_posts_list(request):
    keyword = request.GET.get("keyword")
    naver_posts = NaverPost.objects.all()

    if keyword:
        naver_posts= naverPost.objects.filter(keyword=keyword)

    return render(
        request,
        "naver_posts/list.html",
        {
            "keyword": keyword,
            "naver_posts": naver_posts,
        },
    )
