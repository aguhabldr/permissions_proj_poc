from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Project

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'