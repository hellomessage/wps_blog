import json
import requests

from django.http.response import HttpResponse
from django.template import loader

def home(request):
	template = loader.get_template("home.html")
	return HttpResponse(
		template.render(
			{"site_name" : "wps blog"},
			request,
		)
	)

def room(request, room_id):
	#방 번호 ( room_id ) 직방의 데이터를 그대로 보여주는 뷰(컨트롤러)
	url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
	response = requests.get(url)
	return HttpResponse(
		response.content,
		content_type="application/json", #json형식으로변환
	)

def news(request):
	search = request.GET.get("search")	#html에서 get으로 넘기는 것을 받아옴 

	response = requests.get("https://watcha.net/home/news.json?page=1&per=50")
	news_dict = json.loads(response.text)	# response.json()
	news_list = news_dict.get("news")

	if search:
		news_list = list(filter(
			lambda news: search in news.get('title'),
			news_list,
		))

	template = loader.get_template("news.html")	
	return HttpResponse(
		template.render(
			{ "news_list" : news_list },
			request,
		)
	)
