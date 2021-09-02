from django.shortcuts import render, redirect
from .models import product,cart  # importing models from model file
from django.contrib import messages  # importing messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import pizza_choiceSerializer,cart_Serializer,pizza_Serializer  # import pizza_choice form seializer file.
from rest_framework import generics
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


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

# post the data 
@csrf_exempt
def pizza_post(request): # craeting api for the all feilds
    if  request.method == 'POST': # post  request post the data
        data = JSONParser().parse(request)
        serializer = pizza_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)# when wrong data is send server return 400 insead of 500
