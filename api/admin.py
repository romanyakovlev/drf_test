from django.contrib import admin
from api.models import Post, PostLike, ActivityProfile
# Register your models here.

admin.site.register([Post, PostLike, ActivityProfile])