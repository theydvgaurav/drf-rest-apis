from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from post.permissions import AuthorOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,AuthorOrReadOnly]
    

    def create(self, request):
        request.data['author'] = request.user.id
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Post Created Successfully",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



