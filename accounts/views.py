from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, response, status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from restapis.colors import bcolors
from rest_framework.decorators import action

class UserSignUpView(GenericViewSet,mixins.CreateModelMixin,):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    @action(methods=['POST'], detail=False)
    def register(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)



class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})