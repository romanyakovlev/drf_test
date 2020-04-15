from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now = True)

class PostLike(models.Model):
    person = models.ForeignKey(User,related_name='person_like', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Post,null=True,related_name='likes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now = True)


class PostDislike(models.Model):
    person = models.ForeignKey(User,related_name='person_dislike', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Post,null=True,related_name='dislikes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now = True)

class ActivityProfile(models.Model):
	person = models.OneToOneField(User, on_delete=models.CASCADE)
	last_activity = models.DateTimeField(auto_now = True)

