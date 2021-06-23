from django.shortcuts import render, redirect
from .models import product  # importing models from model file
from django.contrib import messages  # importing messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import pizza_choiceSerializer  # import pizza_choice form seializer file.
from rest_framework import generics
from django.http import HttpResponse,JsonResponse


def pizza_choiceList(request):
    if request.method == "GET": # get request to fetch the data 
        pizza_choice =  product.objects.all()
        serializer = pizza_choiceSerializer(pizza_choice, many=True)
        return JsonResponse(serializer.data, safe=False)


# fecthing the data according to the id

def pizza_detail(request, pk):
    try:
        pizza_choice_id = product.objects.get(pk=pk)
    except pizza_choice_id.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET': # get request to fetch all the data according to the id
        serializer = pizza_choiceSerializer(pizza_choice_id)
        return JsonResponse(serializer.data)