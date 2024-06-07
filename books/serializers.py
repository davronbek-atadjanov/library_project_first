from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


# ModelSerializer
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # Check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "Status":"Error",
                    "message":"title if it contains only alphabetical chars"
                }
            )

        # check title and author from database existance
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "Status":"Error",
                    "message":"title and author database is valid"
                }
            )
        return data
    def validate_isbn(self, attr):
        if Book.objects.filter(isbn=attr).exists():
            raise ValidationError(
                {
                    "status":"False",
                    "message":"isbn uncal "
                }
            )

        return attr
# Serializer

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=150)
#     content = serializers.CharField()
#     author = serializers.CharField()
#     isbn = serializers.CharField()
#     price = serializers.CharField()

