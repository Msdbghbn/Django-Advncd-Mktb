from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import time 
from .tasks import sendEmail
import requests
from django.core.cache import cache 

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get("https://87faf5ed-d0d1-4761-82ac-04dfdc382f6c.mock.pstmn.io/test/delay/5")
        cache.set("test_delay_api",response.json(),60)
    return JsonResponse(cache.get("test_delay_api"))
