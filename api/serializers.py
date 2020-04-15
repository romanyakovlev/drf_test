from django.contrib.auth.models import User
from api.models import Post, PostLike
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.decorators import action
from rest_framework.response import Response


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['text', 'author', 'date', 'likes', 'dislikes']
		extra_kwargs = {
            'author': {'read_only': True},
        }

	def create(self, validated_data):
		validated_data['author'] = self.context['request'].user
		print(validated_data)
		author_post = Post(**{'author': validated_data['author'], 'text': validated_data['text']})
		author_post.save()
		return author_post

	def to_representation(self, instance):

		ret = super().to_representation(instance)
		ret['likes'], ret['dislikes'] = len(ret['likes']), len(ret['dislikes'])
		return ret

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['person', 'tweet', 'date']