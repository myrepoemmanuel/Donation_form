import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Donator
from django.contrib import messages

# Create your views here

def home(request):
    donations = Donator.objects.all()
    context = {"donations":donations}
    return render(request, 'aform/home.html', context)


def processDonation(request):
    data = json.loads(request.body)
    Donator.objects.create(
    name=data['userPayData']['name'],
    amount=data['userPayData']['amount'], 
    )
    print(data)
    return JsonResponse('payment complete', safe=False)

