from django.shortcuts import render
from django.utils.decorators import decorator_from_middleware
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


def depthome(request):
    if request.user.user_type != 2:
        raise PermissionDenied()
    return HttpResponse("Hello DepartmentPerson!")
