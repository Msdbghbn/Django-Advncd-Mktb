from django.urls import is_valid_path
from rest_framework.decorators import api_view, permission_classes,action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer,CategorySerializer
from ...models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets

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

class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)





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



class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    lookup_field='id'

class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self,request):
        serializer=self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        post_object=get_object_or_404(self.queryset,pk=pk)
        serializer=self.serializer_class(post_object)
        return Response(serializer.data)

    # other CURDE functions also like that. So we did not completed them and used 'Response('ok')' only.
    def create(self, request):
        return Response('ok')
    def retrieve(self, request, pk=None):
        return Response('ok')
    def update(self, request, pk=None):
        return Response('ok')
    def partial_update(self, request, pk=None):
        return Response('ok')
    def destroy(self, request, pk=None):
        return Response('ok')
'''

class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    @action(methods=['get'],detail=False)
    def get_ok(self,request):
        return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
