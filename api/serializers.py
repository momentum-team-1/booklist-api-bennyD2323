from rest_framework import serializers
from api.models import User, Book, Note


class UserSerializer(serializers.HyperlinkModelSerializer):

    class Meta:
        model = User
        fields = [
            'date_joined',
        ]


class BookSerializer(serializers.HyperlinkModelSerializer):

    class Meta:
        model = Book
        fields = [
            'user',
            'status',
            'author',
            'title',
        ]

class NoteSerializer(serializers.HyperlinkModelSerializer):

    class Meta:
        model = Note
        fields = [
            'created_at',
            'body',
            'page_num',
        ]


