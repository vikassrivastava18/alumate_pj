from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, PostComment, PostLike, PostCommentLike
from . import serializers

# list
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

# create
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCommentListView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = serializers.PostCommentCreateSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.pop('pk'))
        return post.comments

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post = get_object_or_404(Post, pk=self.kwargs.pop('pk'))
        post_comment = PostComment.objects.create(
            user = request.user,
            post = post,
            body = serializer.validated_data['body'],
            image = serializer.validated_data.get('image', None)
        )
        serializer = serializers.PostCommentSerializer(instance=post_comment)
        
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class PostLikeListView(APIView):
    serializer_class = serializers.PostLikeSerializer
    
    def get(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(post.likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        try:
            post_like = PostLike.objects.get(user=user, post=post)
            serializer = self.serializer_class(post_like)
            return Response(serializer.data, status=status.HTTP_303_SEE_OTHER)
        except PostLike.DoesNotExist: # normal case
            post_like = PostLike.objects.create(user=user, post=post)
            serializer = self.serializer_class(post_like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostCommentLikeListView(APIView):
    serializer_class = serializers.PostCommentLikeSerializer

    def get(self, request, pk=None):
        post_comment = get_object_or_404(PostComment, pk=pk)
        serializer = self.serializer_class(post_comment.likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        user = request.user
        comment = get_object_or_404(PostComment, pk=pk)
        try:
            post_comment_like = PostCommentLike.objects.get(user=user, comment=comment)
            serializer = self.serializer_class(post_comment_like)
            return Response(serializer.data, status=status.HTTP_303_SEE_OTHER)
        except PostCommentLike.DoesNotExist: # normal case
            post_comment_like = PostCommentLike.objects.create(user=user, comment=comment)
            serializer = self.serializer_class(post_comment_like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# detail view
class PostDetailView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_pk = kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, pk=obj_pk)


class PostCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = serializers.PostCommentSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_pk = kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, pk=obj_pk)


class PostLikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = serializers.PostLikeSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_pk = kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, pk=obj_pk)


class PostCommentLikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostCommentLike.objects.all()
    serializer_class = serializers.PostCommentLikeSerializer

    def get_object(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        obj_pk = kwargs.pop('pk')
        user = self.request.user
        return get_object_or_404(queryset, user=user, pk=obj_pk)
