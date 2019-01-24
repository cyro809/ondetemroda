from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://localhost:8080/events')
    rodas = r.json()

    return render(request, 'rodas/index.html', { 'rodas': rodas})