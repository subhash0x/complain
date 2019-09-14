from myauth.models import User
from django.core.exceptions import PermissionDenied

class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.user_type != 1:
            raise PermissionDenied()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
