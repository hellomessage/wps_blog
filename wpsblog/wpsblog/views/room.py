import requests

from django.http.response import HttpResponse


def room(request, rooo_id):
    url = "https//api.zigbang.com/v1/items?detail=true&item_ids=" + roomid
    response = requests.get(url)
    return HttpResponse(
        response.content,
        content_type="application/json",
        )
