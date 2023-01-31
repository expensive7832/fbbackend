from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from .serializer import userSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

class userLogic(APIView):

    def post(self, request):

        data = request.data

        serializer = userSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

            return Response(data="success")
        else:
            return Response(data=serializer.errors)


class Login(APIView):
    def post(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email = email, password = password ).first()
        
        

        if user is not None:
            refresh = RefreshToken.for_user(user)

            
            data = {
                "token": str(refresh.access_token),
                "message": "login successful"
            }
            return Response(data = data, status=status.HTTP_200_OK)
        else:
            return Response(data = {"message": "No credentials Found"}, status=status.HTTP_200_OK)    

