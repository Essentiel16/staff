from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Users


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class UserList(APIView):
    def get(self, request):
        model = Users.objects.all()
        # model2 = Department.objects.all()
        serializer = UsersSerializer(model, many=True)
        # if serializer.is_valid():
        # serializer.save()
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    def get_user(self, firstName):
        try:
            model = Users.objects.get(id=firstName)
            return model
        except Users.DoesNotExist:
            return Response(f'{firstName} id Not Found in the database', status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        model = self.get_user(data=request.data)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)