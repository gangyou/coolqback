from django.shortcuts import HttpResponse
from django.core import serializers
from django.utils import simplejson
from models import Event

# query event list
def index(request):
    events = Event.objects.all()
    results = []
    for event in events:
        result = {}
        result['id'] = event.id
        result['name'] = event.name
        result['week'] = event.week
        result['item'] = event.item
        results.append(result)
    data = simplejson.dumps(results)
    return HttpResponse(data, mimetype="applicatoin/json")