from api.models import  *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from api.serializers import MetadataSerializer
from api.headers import *


# Create your views here.
class Metadataviewset(CompactViewSet):
    permission_classes = (IsAuthenticated) 
    queryset= Metadata.objects.all()
    serializer_class = MetadataSerializer

    def list(self,request):
        pass


    # def list(self, request,):
    #     snippets = Metadata.objects.all()
    #     serializer = MetadataSerializer(snippets, many=True)
    #     return Response(serializer.data)

    # def get_object(self, pk):
    #     try:
    #         return Metadata.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404