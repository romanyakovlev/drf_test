from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
from api.models import Post, PostLike, PostDislike, ActivityProfile
from api.serializers import UserSerializer, PostSerializer, PostLikeSerializer

import datetime


class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

	@action(detail=True, methods=['get'])
	def activity(self, request, pk, format=None):

		last_login = User.objects.get(pk=pk).last_login
		last_activity = ActivityProfile.objects.get(
			person=User.objects.get(pk=pk)).last_activity
		content = {
			'last_login': last_login, 
			'last_activity': last_activity,
		}

		return Response(content)
		

class PostViewSet(viewsets.ModelViewSet):

	queryset = Post.objects.all()
	serializer_class = PostSerializer

	@action(detail=True, methods=['post', 'get'])
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

	@action(detail=True, methods=['post', 'get'])
	def dislike(self, request, *args, **kwargs):

		post = self.get_object()
		if not any(post.dislikes.filter(person=request.user).all()):
			dislike = PostDislike(tweet=post, person=request.user)
			dislike.save()
			if any(post.likes.filter(person=request.user).all()):
				post.likes.filter(person=request.user).delete()
			content = {'message':'post has been disliked'}
			return Response(content)
		else:
			content = {'message':'post had been already liked'}
			return Response(content)


from rest_framework.views import APIView


class AnaliticsView(APIView):
	
	def get(self, request, format=None):
		try:
			date_from = datetime.datetime.strptime(request.query_params['date_from'], "%Y-%m-%d").date()
			date_to = datetime.datetime.strptime(request.query_params['date_to'], "%Y-%m-%d").date()
			if date_from > date_to: 
				content = {'message':'from_date is older than to_date. try again.'}
		except Exception as e:
			content = {'message':'error invalid date. try again.'}
			return Response(content)

		likes = request.user.person_like.filter(date__range=(date_from, date_to)).count()
		dislikes = request.user.person_dislike.filter(date__range=(date_from, date_to)).count()
		content = {'Analitics of like/dislke amount from your account from {} to {}'.format(
						date_from, date_to
					): {'likes': likes, 'dislikes': dislikes}
				  }
		return Response(content)	