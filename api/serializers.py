from rest_framework import serializers
from api.models import User, Book, Note, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name'
        ]

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

class BookSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     user = Book.objects.create(**validated_data):

    class Meta:
        model = Book
        fields = [
            'id',
            'url',
            'user',
            'status',
            # 'author',
            'title',
            # 'notes',
        ]
    

