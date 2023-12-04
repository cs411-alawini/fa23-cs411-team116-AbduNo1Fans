from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import MyModel

def get_data(request):
    data = list(MyModel.objects.values())
    return JsonResponse({'data': data})
