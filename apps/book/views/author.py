
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView
from apps.book.models import Author
from apps.book.serializers import AuthorSerializer

# Function-base view
@api_view(['GET']) # by default , it uses a 'GET' method
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_authors(request):
    # get all authors using ORM
    authors = Author.objects.all()

    # deserializer using the AuthorSerializer
    data = AuthorSerializer(authors, many=True)

     # Return data
    return Response(data.data, status=status.HTTP_200_OK)
"""
curl http://127.0.0.1:8000/api/v1/book/author/1

curl -u admin:admin  http://127.0.0.1:8000/api/v1/book/author/1
"""
class DetailAuthor(RetrieveDestroyAPIView):
    # how do we handle generics views

    # ORM
    queryset = Author.objects.all()

    # serializer
    serializer_class = AuthorSerializer
    
    # Authentication: declare an authentication schem to be used
    authentication_classes=(BasicAuthentication,)

    # permissions: IsAuthenticated triggers the authentication proces to take place 
    permission_classes = (IsAuthenticated,)

class DeleteAuthor(DestroyAPIView):
    # ORM
    queryset = Author.objects.all()

    # serializer
    serializer_class = AuthorSerializer



