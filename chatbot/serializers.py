from rest_framework import serializers
from chatbot.models import BookChunk, Book


class BookChunkSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookChunk
        fields = ('chunk_id', 'content')

class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author')
