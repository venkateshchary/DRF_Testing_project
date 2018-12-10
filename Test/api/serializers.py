from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Metadata


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password':{'write_only' : True, 'required' : True}}
    
    def create(self,validated_data):
    	user = User.objects.create_user(**validated_data)
    	return user


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ('SKU', 'NAME', 'LOCATION', 'DEPARTMENT', 'CATEGORY', 'SUBCATEGORY')