from django.contrib import admin
from api.models import Post, PostLike, PostDislike
# Register your models here.

admin.site.register([Post, PostLike, PostDislike])