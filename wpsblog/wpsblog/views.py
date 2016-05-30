import json
import request

from django.http.response import HttpResponse
from djando.shortcuts import render



def home(request):
	return render(
		"home.html",
		{ "site_name" : "wps blog"}
	)

#	templete = loader.get_template("home.html")
#
#	return HttpResponse(
#		templte.rander(
#			{"site_name" : "wps blog")},
#			request,
#		)	
#	)
#
def room(request, rooo_id):
	url = "https//api.zigbang.com/v1/items?detail=true&item_ids=" + roomid
	response = requests.get(url)
	return HttpResponse(
		response.content,
		content_type="application/json",
	)

def news(request):
	search = request.GET.get("search")

	response = request.get("https://watcha.net/home/news.json?page=18&per=50")
		news_dict = json.loder(response.text)
		new_list = news_dict.get("news")

		if search:
			news_list = list(filter(
				lambda news: search in news.get('title'),
				news_list,
			))

		return render(
			request,
			"news.html",
			{"news_list" : news_list},
		)
#		template = loader.get_template("news.html")
#		return HttpResponse((
#				template.rander(
#					{"news_list" : news_list},
#					request,
#			)
#		)
