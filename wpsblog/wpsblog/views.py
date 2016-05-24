from django.conf.urls import url~
from django.http.response import HttpResponse 

from wpsblog.views import home, room

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^$', home),
	url(r'rooms/(?P<room_id>\d+)\$', room),
]

from django.http.response import HttpResponse

def home(request):
	return HttpResponse("hello world")

def room(request, room_id):
	url = "" + room_id
	response = requests.get(url)
	return HttpResponse(
			response.content,
			content_type="application/json",
	)
