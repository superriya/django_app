from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .serializers import PostSerializer
from .models import Post

# Create your views here.
def listOverview(request):
    # return JsonResponse("API BASE POINT", safe=False)
    posts = Post.objects.all()
    context = {
        "posts" : posts 
    }
    return render(request, 'home.html', context)



@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)
    
    # try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExits:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == "GET":
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_Valid():
        serializer.save()

    return Response(serializer.data)