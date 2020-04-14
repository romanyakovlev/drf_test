from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from api.models import Post, PostLike, PostDislike
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, PostSerializer, PostLikeSerializer
from rest_framework.decorators import action
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):

	queryset = Post.objects.all()
	serializer_class = PostSerializer

	@action(detail=True)

	def like(self, request, *args, **kwargs):

		post = self.get_object()
		if not any(post.likes.filter(person=request.user).all()):
			like = PostLike(tweet=post, person=request.user)
			like.save()
			if any(post.dislikes.filter(person=request.user).all()):
				post.dislikes.filter(person=request.user).delete()
			content = {'message':'post has been liked'}
			return Response(content)
		else:
			content = {'message':'post had been already liked'}
			return Response(content)

	@action(detail=True)

	def dislike(self, request, *args, **kwargs):

		post = self.get_object()
		if not any(post.dislikes.filter(person=request.user).all()):
			like = PostDislike(tweet=post, person=request.user)
			like.save()
			if any(post.likes.filter(person=request.user).all()):
				post.likes.filter(person=request.user).delete()
			content = {'message':'post has been disliked'}
			return Response(content)
		else:
			content = {'message':'post had been already liked'}
			return Response(content)

class PostLikeViewSet(viewsets.ModelViewSet):

	queryset = PostLike.objects.all()
	serializer_class = PostLikeSerializer