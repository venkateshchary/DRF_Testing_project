from rest_framework import status
from django.db import IntegrityError
from django.db import transaction
from rest_framework import mixins
from api.models import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import  permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from rest_framework import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.db.models import Max
import re
import sys
#from api.vouchermanager import *


#import logging
from rest_framework import viewsets
from decimal import *

from api.models import *

class CompactViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    pass

class CRViewSet(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    pass


def resource_access_handler(request, resource):
    """ Callback for resource access. Determines who can see the documentation for which API. """
    # Superusers and staff can see whatever they want
    if request.user.is_superuser or request.user.is_staff:
        return True
    else:
        if isinstance(resource, str):
            try:
                resolver_match = resolve('/{}/'.format(resource))
                view = resolver_match.func
            except Exception:
                return False
        else:
            view = resource.callback

        view_attributes = view.func_dict
        feature_flag = view_attributes.get('feature_flag')
def swaggeruser():
    return User.objects.get(pk=5)
