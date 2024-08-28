from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.book.models import Tag 
from apps.book.serializers import TagSerializer

""""
curl http://127.0.0.1:8000/api/v1/book/tag/
token_header ='Authorization: Token 6ecd686b07a2ba70ba3a7dd1eceacc9ed0f315ae'
curl -H 'Authorization: Token 6ecd686b07a2ba70ba3a7dd1eceacc9ed0f315ae' http://127.0.0.1:8000/api/v1/book/tag/
"""

@api_view()# define our http methode
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_tags(request): # JSONParser

    # ORM
    tags = Tag.objects.all() # complet data type

    # DeSerializations
    data = TagSerializer(tags, many=True) # convert complex data type to primitive types
     # return json
    return Response(data.data, status=status.HTTP_200_OK)