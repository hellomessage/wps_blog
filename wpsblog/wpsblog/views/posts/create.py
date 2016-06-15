from django.shortcuts import redirect

from wpsblog.models import Post


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.FILES.get("image")

    print(title)
    print(content)
    print(image)

#    from IPython import embed; embed()

    post = Post.objects.create(
        title=title,
        content=content,
        image=image,
    )
     
    return redirect(post)
