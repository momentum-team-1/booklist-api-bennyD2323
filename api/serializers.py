from rest_framework import serializers
from api.models import User, Book, Note


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'date_joined',
        ]


class BookSerializer(serializers.ModelSerializer):
    notes = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = [
            'id',
            'url',
            'user',
            'status',
            'author',
            'title',
            'notes',
        ]

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            'created_at',
            'body',
            'page_num',
            'note',
            'book',
        ]


