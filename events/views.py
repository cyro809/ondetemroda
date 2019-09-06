from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://localhost:3000/events')
    events = r.json()

    return render(request, 'events/index.html', { 'events': events, 'locations': get_locations_coordinates(events)})

def get_locations_coordinates(events):
    locations = []
    for event in events:
        locations.append([
            event.get('NomeEvento'),
            event.get('Latitude'),
            event.get('Longitude'),
            1
        ])
    return locations