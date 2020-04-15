from api import views
from django.urls import include
from django.conf.urls import url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^analitics/', views.AnaliticsView.as_view()),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),

]
