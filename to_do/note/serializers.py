from django.contrib.auth.models import User
from note.models import Note, List
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url','id','username','email']


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ['user','list','title','desc','due','done']

class ListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = List
        fields = ['user','name']
