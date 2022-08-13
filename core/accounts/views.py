from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import time 
from .tasks import sendEmail
import requests

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

def test(self):
    response=requests.get("https://87faf5ed-d0d1-4761-82ac-04dfdc382f6c.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())
