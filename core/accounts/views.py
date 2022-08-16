# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import time
from .tasks import sendEmail
import requests
# from django.core.cache import cache
from django.views.decorators.cache import cache_page


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")


@cache_page(60)
def test(request):
    response = requests.get(
        """https://87faf5ed-d0d1-4761-82ac-04dfdc382f6c.mock.pstmn.io/
        test/delay/5"""
    )
    return JsonResponse(response.json())
