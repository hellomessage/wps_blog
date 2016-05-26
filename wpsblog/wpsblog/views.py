import json
import requests

from django.http.response import HttpResponse
from django.conf import settings

def home(request):
	return HttpResponse("<h1>hello world</h1><p>This is home page.</p>")

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

	with open(settings.BASE_DIR + "/wpsblog/templates/news.html", "r") as template:
		content = template.read()
		content +="<p>{count} 개의 영화 뉴스 정보가 있습니다.</p>".format(count=len(news_list)) +\
		"".join([
			"<h2>{title}</h2><img src={image_src}><p>{content}</p>".format(
				title=news.get('title'),
				image_src=news.get('image'),
				content=news.get('content'),
			)
			for news
			in news_list
		])
 
		return HttpResponse(
			content
		)

