from django.shortcuts import render
from api.models import Metadata
from api.serializers import MetadataSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import re
import logging
import jwt
from functools import wraps
from Test import settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


def token_required(f):  
    @wraps(f)
    def decorated(request,format=None):
        print("requets headers:",request.headers)
        token = None
        if 'token' in request.headers:
            token = request.headers['token'].strip()
        if not token:
            return Response({'message':"token missing"})
        try:
            data = jwt.decode(token,settings.SECRET_KEY)
            print("print out the data :",data)
        except:
            return  Response(serializer.data,  status=status.HTTP_400_BAD_REQUEST)
        return f(request,format=None)
    return decorated

class MetadataList(APIView):

    
    def get(self, request,format=None):
        location = Metadata.objects.all()
        serializer = MetadataSerializer(location, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return Metadata.objects.get(LOCATION=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = MetadataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Locationdept(APIView):
    '''
    list all departments 
    '''
    @token_required
    def get(self,request,location_id, format=None):
        try:
            queryset= Metadata.objects.filter(LOCATION=location_id)
            locations = MetadataSerializer(queryset, many=True)
            return Response(locations.data,status= status.HTTP_201_CREATED)
        except:
            raise

    def post(self, request, location_id,format=None):
        serializer = MetadataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Departments(APIView):
    '''
    list all departments 
    '''
    def get(self,request,location_id,department_id, format=None):
        try:
            queryset= Metadata.objects.filter(Q(LOCATION=location_id)& Q(DEPARTMENT=department_id))
            departments = MetadataSerializer(queryset, many=True)
            return Response(departments.data,status= status.HTTP_201_CREATED)
        except:
            raise
class Category(APIView):
    '''
    list all departments 
    '''
    def get(self,request,location_id,department_id,category_id, format=None):
        try:
            if "Ê" in department_id:
                department_id = department_id.replace("Ê",'')
            if "Ê" in category_id:
                category_id = category_id.replace("Ê",'')
            print(department_id,category_id)
            queryset= Metadata.objects.filter(Q(LOCATION=location_id) & Q(DEPARTMENT=department_id)&Q(CATEGORY= category_id))
            category = MetadataSerializer(queryset, many=True)
            return Response(category.data,status= status.HTTP_201_CREATED)
        except:
            raise

class Subcategory(APIView):
    '''
    list all subcategory 
    '''
    def get(self,request,location_id,category_id,department_id,subcategory_id, format=None):
        try:
            print("---------------------------------------------")
            if "Ê" in department_id:
                department_id = department_id.replace("Ê",'')
            if "Ê" in category_id:
                category_id = category_id.replace("Ê",'')
            if "Ê" in subcategory_id:
                subcategory_id = subcategory_id.replace("Ê",'')
            print(location_id,department_id,category_id,subcategory_id,)
            queryset= Metadata.objects.filter(Q(LOCATION=location_id)& Q(DEPARTMENT=department_id)& Q(CATEGORY= category_id)&Q(SUBCATEGORY=subcategory_id))
            subcategory = MetadataSerializer(queryset, many=True)
            return Response(subcategory.data,status= status.HTTP_201_CREATED)
        except:
            raise