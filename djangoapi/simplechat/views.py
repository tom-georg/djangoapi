
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ChatBeitrag
from rest_framework import viewsets

class ChatBeitragSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatBeitrag
        fields = ['username', 'text', 'created_at', 'updated_at']
        #read_only_fields = ['created_at', 'updated_at']


class ChatBeitragViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ChatBeitrag.objects.all().order_by('-created_at')
    serializer_class = ChatBeitragSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


