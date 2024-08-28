# TODO: create a custom permission that will make sure that 
# it check the authenticated user id is the sake as the reader user id.

from rest_framework. permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# isauthenticated ->  if user is not authenticated , it wil fail 
# IsAdminUser -> 'is_staff is 'False' , it will fail
# IsAuthenticatedPrReadOnly -> CRUD
# POST
# GET
# PUT, PATCH 
# DELETE
