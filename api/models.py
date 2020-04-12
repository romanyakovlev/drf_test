from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.CharField(max_length = 140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now = True)


class PostLike(models.Model):
    person = models.ManyToManyField(User,related_name='person_liked')
    tweet = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE,)


class PostDislike(models.Model):
    person = models.ManyToManyField(User,related_name='person_unliked')
    tweet = models.ForeignKey(Post,null=True,related_name='dislikes', on_delete=models.CASCADE,)
