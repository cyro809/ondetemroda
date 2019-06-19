from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://localhost:3000/events')
    events = r.json()
    locations = []
    for event in events:
        location = [
            event.get('NomeEvento'),
            event.get('Latitude'),
            event.get('Longitude'),
            1
        ]
        locations.append(location)

    return render(request, 'events/index.html', { 'events': events, 'locations': locations})