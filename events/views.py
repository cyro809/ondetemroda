from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://localhost:8080/events')
    events = r.json()

    return render(request, 'events/index.html', { 'events': events})