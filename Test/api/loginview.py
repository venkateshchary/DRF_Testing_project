from rest_framework_jwt.settings import api_settings
import sys
import requests
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from datetime import datetime,timedelta
import urllib
from django.contrib.auth.models import User
from django.contrib.auth.models import *
import django.contrib.auth.models
from Test import settings
import logging
from api.models import *
import jwt


@api_view(['POST'])
@csrf_exempt
def user_login(request):
    mandatory_fields =('username','password') 
    print("------------------------------------------------------")
    print(request.data)
    for field in mandatory_fields:
        if field not in request.data:
            return HttpResponse(content={'reason':field},status=status.HTTP_200_OK)
    
    rd = request.data
    ts =datetime.now()
    uname = rd['username']
    passw = rd['password']
    
    user = authenticate(username=uname, password=passw)
    if user is not None:
        if user.is_active:
            print("in of ============================")
            try:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s" % (user.email)
                user_details['token'] = token
                user_details["session"]= request.session.session_key
                user_details["csrf"]= django.middleware.csrf.get_token(request)
    # return Response({"token": token.key})
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                    raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
