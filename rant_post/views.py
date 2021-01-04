import logging

from rest_framework import generics
from .serializers import RantPostSerializer
from .models import RantPost
from rest_framework.permissions import IsAuthenticated
from .permissions import RantPostUpdateDeletePermissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class RantPostListCreateView(generics.ListCreateAPIView):
    serializer_class = RantPostSerializer
    queryset = RantPost.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RantPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RantPostSerializer
    queryset = RantPost.objects.all()
    permission_classes = [IsAuthenticated, RantPostUpdateDeletePermissions]


class UserPostsView(APIView):
    """ Fetch all posts specific to a User """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        try:
            id = request.user.id
            user_posts = RantPost.objects.filter(author=id)
            user_posts_serializer = RantPostSerializer(user_posts, many=True)
            
            logging.getLogger('root').debug(f'posts fetched for user with id {id} ')

            return Response(user_posts_serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            logging.getLogger('root').error(str(e))
            return Response({'message': 'some error occured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
