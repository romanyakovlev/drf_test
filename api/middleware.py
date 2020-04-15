from django.utils import timezone

from api.models import ActivityProfile
from django.utils.deprecation import MiddlewareMixin

class UpdateLastActivityMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), 'Last Activity Middleware'
        if request.user.is_authenticated:
            ActivityProfile.objects.filter(person__id=request.user.id).update(last_activity=timezone.now())