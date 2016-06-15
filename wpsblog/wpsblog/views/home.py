from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse
'''
#from django.views.generic import TemplateView
#
#
#lass HomeView(TemplateView):
#
#   template_name = "home.html"
#
#   def get_context_data(self, **kwargs):
#       context = super(HomView, self).get_context_data(**kwargs)
#       context["site_name"] = "wps blog"
#       return context
#class HomeView(View):
#
#    def get(self, request, *agrs, **kwargs):
#        return render(
#            request,
#            "home.html",
#            {"site_name": "wps blog"},
#        )
'''

'''
def home(request):
    return render(
        request,
        "home.html",
        {"site_name": "wps blog"},
    )
'''

def home(request):
    return render(
        request,
        "home.html",
        {"site_name": "wps blog"},
    )
