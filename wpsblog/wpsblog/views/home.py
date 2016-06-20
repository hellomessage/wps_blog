from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["site_name"] = "wps blog"
        return context
#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             "home.html",
#             {"site_name": "wps blog"},
#         )
# def home(request):
#     return render(
#         request,
#         "home.html",
#         {"site_name": "wps blog"},
#     )
