# help in authenticating the user against username and password
from django.contrib.auth import authenticate 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from apps.reader.models import Reader
from apps.reader.serializers import ReaderSerializer


class Login(APIView):

    def post(self, request):
        # extract credentials
        password = request.data.get('password')
        username = request.data.get('username')

        # auhtenticate the user 
        user: User | None = authenticate(
            username=username,
            password=password
        )
         
         # generate token
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'error': 'Invalid_credential',
                'detail': 'username or password is incorrect'},
                status=status.HTTP_404_NOT_FOUND
                )




# class DetailReader(APIView):
#     def get(self, request):
#         pass


# api/v1/reader/1
@api_view()
def detail_rader(request, pk):
    # get reader by pk
    reader =Reader.objects.get(user_id=pk) # data type
    

    # deserialization my reader
    # data={
    #     "id": reader.user.id,
    #     "user":{
    #         "user_id": reader.user.username
    #     }
    # }

    data = ReaderSerializer(reader)

    return Response({'data': data.data})