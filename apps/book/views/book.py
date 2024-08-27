# List book -> GET
# Create  -> POST
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Book, Author
from apps.book.serializers import ReadBookSerializer, CreateBookSerializer
from rest_framework.views import APIView


# List Book
@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()

    data = ReadBookSerializer(books, many=True)

    return Response(data.data, status=status.HTTP_200_OK)


# Create Book
@api_view(['POST'])
def create_book(request):
    with transaction.atomic():
        data = request.data # retrieve the request body in native Python data type

        authors = data['authors']

        book = CreateBookSerializer(data=data)

        book.is_valid()
        saved_book = book.save()

        # Add authors
        for author in authors:
            author_obj = Author.objects.get(pk=author['id'])
            saved_book.authors.add(author_obj, through_defaults={'role': author['role']})

    # Return a JSON transformed data
    return Response({'isbn': saved_book.isbn}, status=status.HTTP_201_CREATED)

    #return Response({'detail': 'Invalid request data', 'error': 'Invalid_Request'}, status=status.HTTP_400_BAD_REQUEST)

class BooksView(APIView):
    # GET
    def get(self, request):
        books = Book.objects.all()

        # deserializations
        data = ReadBookSerializer(books, many=True)

        return Response({'data': data.data}, status=status.HTTP_200_OK)


    def post(self, request):
        pass

    def delete(self, request):
        pass

    def gput(self, request):
        pass

    def patch (self, request):
        pass





