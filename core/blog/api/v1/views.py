from django.urls import is_valid_path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


'''
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == "GET":
        #posts=Post.objects.all()
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''

class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request):
        posts=Post.objects.filter(status=True)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


'''
@api_view(['GET','PUT','DELETE'])
def post_detail(request,id):
    post=get_object_or_404(Post,pk=id,status=True)
    if request.method == "GET":
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({'detail':'Item remove successfully'},status= status.HTTP_204_NO_CONTENT)

'''

class PostDetail(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer

    def get(self,request,id):
        post=get_object_or_404(Post,pk=id,status=True)
        serializer=PostSerializer(post)
        return Response(serializer.data)

    def put(self,request,id):
        post=get_object_or_404(Post,pk=id,status=True)
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    def delete(self,request,id):
        post=get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({'detail':'Item remove successfully'},status= status.HTTP_204_NO_CONTENT)

