from django.contrib import admin
from api.models import Post, PostLike
# Register your models here.

admin.site.register([Post, PostLike])