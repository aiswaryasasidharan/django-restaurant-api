from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class SignupAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        login(request, user)
        return Response({"message": "Logged in"})

