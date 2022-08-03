from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(["GET","POST"])
def post_list(request):
    if request.method == "GET":
        #posts=Post.objects.all()
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view()
def post_detail(request,id):
    post=get_object_or_404(Post,pk=id,status=True)
    serializer=PostSerializer(post)
    return Response(serializer.data)

