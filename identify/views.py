from django.shortcuts import render
from .models import Identify
import json
from django.http import JsonResponse


# Create your views here.

def UuidApi(request):
    Identify.objects.create()
    response = {}
    for entity in Identify.objects.all().order_by('-created'):
        response[str(entity.created.strftime('%Y-%m-%d %H:%M:%S.%f}'))] = str(entity.id)
    return JsonResponse(response, safe=False)    


