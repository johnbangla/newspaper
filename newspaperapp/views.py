from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bangla,English,Video
from .serializers import EnglishSerializer,BanglaSerializer,VideoSerializer



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List1': '/englistings/',
        'List2': '/bdlistings/',
        'List3': '/videolistings/',
       
     
    }

    return Response(api_urls)






#Fething complex data for mobile 
@api_view(['GET'])
def engtaskList(request):
    tasks = English.objects.all().order_by('-id')
    serializer = EnglishSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bdtaskList(request):
    tasks = Bangla.objects.all().order_by('-id')
    serializer = BanglaSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def videotaskList(request):
    tasks = Video.objects.all().order_by('-id')
    serializer = VideoSerializer(tasks, many=True)
    return Response(serializer.data)