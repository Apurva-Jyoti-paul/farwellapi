import contextlib
from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapp.serializers import SeniorSerializer,SeniorinfoSerializer,awardsSerializer,imagegallerySerializer
from .models import Seniorinfo,Senior,awards,imagegallery, ratings


def home(request):
    #if request.method=='POST'
    seniors= Senior.objects.all()
    for i in seniors:
        print(i.dp.url)
    

    return render(request,'webapp/home.html',{})



@api_view(['GET'])
def indv_senior(request,key):
    if request.method == 'GET':
        seniors = Seniorinfo.objects.get(senior__name=key)
        serializer = SeniorinfoSerializer(seniors)
        return Response(serializer.data)




@api_view(['GET'])
def see_seniors(request):
    if request.method == 'GET':
        seniors = Senior.objects.all()
        serializer = SeniorSerializer(seniors,many=True)
        return Response(serializer.data)

# Create your views here.


@api_view(['GET'])
def awrds_senior(request,key):
    if request.method == 'GET':
        award = awards.objects.filter(info__senior__name=key)
       
        serializer = awardsSerializer(award,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def gallery_senior(request,key):
    if request.method == 'GET':

        gallery = imagegallery.objects.filter(desc__senior__name=key)
       
        serializer = imagegallerySerializer(gallery,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def rating_senior(request,key):
    if request.method == 'GET':

        rating = ratings.objects.filter(senior__senior__name=key)
       
        serializer = ratingsSerializer(rating,many=True)
        return Response(serializer.data)



