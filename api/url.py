
from django.contrib import admin
from django.urls import path
from api import views

from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)


urlpatterns = [
	path('^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls'))
]
