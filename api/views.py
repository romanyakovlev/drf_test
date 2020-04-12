from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from api.models import Post
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, PostSerializer
from rest_framework.decorators import action
from rest_framework import status

class HelloView(APIView):
	def get(self, request):
		content = {'message':'Hell0 World'}
		return Response(content)

class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):

	queryset = Post.objects.all()
	serializer_class = PostSerializer

	@action(detail=True)

	def like(self, request, *args, **kwargs):
		kek = PostSerializer(self.get_object(), context={'request': request})
		print(kek)
		return Response(kek.data)

	def dislike(self, request, *args, **kwargs):
		kek = PostSerializer(self.get_object(), context={'request': request})
		print(kek)
		return Response(kek.data)
		