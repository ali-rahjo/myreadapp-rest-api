from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.book.models import Tag 
from apps.book.serializers import TagSerializer

@api_view()# define our http methode
def list_tags(request): # JSONParser
    # ORM
    tags = Tag.objects.all() # complet data type

    # DeSerializations
    data = TagSerializer(tags, many=True) # convert complex data type to primitive types
     # return json
    return Response(data.data, status=status.HTTP_200_OK)