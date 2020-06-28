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

class BookSerializer(serializers.HyperlinkedModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = [
            'url',
            # 'user',
            'status',
            'author',
            'title',
            'notes',
        ]


