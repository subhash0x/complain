from django.shortcuts import render
from django.utils.decorators import decorator_from_middleware
from .middlewares import UserTypeMiddleware
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


def home(request):
    if request.user.user_type != 1:
        raise PermissionDenied()
    return HttpResponse("Hello complain!")
