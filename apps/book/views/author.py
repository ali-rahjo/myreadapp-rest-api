
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.book.models import Author
from apps.book.serializers import AuthorSerializer

# Function-base view
@api_view(['GET']) # by default , it uses a 'GET' method
def list_authors(request):
    # get all authors using ORM
    authors = Author.objects.all()

    # deserializer using the AuthorSerializer
    data = AuthorSerializer(authors, many=True)

     # Return data
    return Response(data,data, status=status.HTTP_200_OK)



