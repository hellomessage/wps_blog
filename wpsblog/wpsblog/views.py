from django.http.response import HttpResponse

#MVC Controller
def home(request):
	return HttpResponse("hello world han's")

def room(requset, room_id):
	print(https://api.zigbang.com/v1/items?detail=true&item_ids=4701501)
	return HttpResponse("This is a room detail" + room_id)
