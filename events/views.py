from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://ec2-3-16-151-208.us-east-2.compute.amazonaws.com:3000/events')
    events = r.json()

    return render(request, 'events/index.html', { 'events': events})