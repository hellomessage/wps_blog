from django.shortcuts import render, ridirect
from django.core.urlresolvers import reverse
from django.views.genetic import View

from bitly.models.bitlink import Bitlink


class BitLinkeCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "bitly/new.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        original_url = request.POST.get("origianl_url")

        bitlink = request.user.bitlink_set.create(
            original_url=original_url,
        )

        bitlink.save()

        return redirect(reverse("home"))
