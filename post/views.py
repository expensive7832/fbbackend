from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import postSerializer
from rest_framework.permissions import IsAuthenticated
from .models import userPost

class postLogic(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request):
      
        data = request.data

        if not (request.data['img'] or request.data['content']):
            return Response(data="Field cannot be empty", status=status.HTTP_406_NOT_ACCEPTABLE)
    
        serializer = postSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [IsAuthenticated]
    def delete(self, request):

        id = request.data['id']

        post_to_del = userPost.objects.filter(id = id).first()

        if post_to_del is not None:
            post_to_del.delete()

            return Response(data="Post Deleted", status=status.HTTP_200_OK)
        return Response(data="Error Deleting Post, Try Again", status=status.HTTP_200_OK)