from django.shortcuts import render
from django.http import JsonResponse
import requests
import json


def home(request):
    news_api_request=requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=7c829a5d95d54c8cb6f90767a089368b")
    print(news_api_request)
    api=json.loads(news_api_request.content)
    return render(request,'index.html',{'api':api})
