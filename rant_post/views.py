import logging

from rest_framework import generics
from .serializers import RantPostSerializer, PostReactSerializer
from .models import RantPost, PostReact
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
    

class PostReactView(APIView):
    """ React to a post """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.user.id
            post_id = request.data['post_id']

            post = RantPost.objects.filter(pk=post_id)
            if not post.exists():
                logging.getLogger('root').error('post not found')
                return Response({'message': 'post not found'}, status=status.HTTP_400_BAD_REQUEST)
            

            reaction = PostReact.objects.filter(user=user_id)
            if reaction.exists():
                logging.getLogger('root').error('reaction removed')
                reaction.delete()
                return Response({'message': 'reaction removed'}, status=status.HTTP_200_OK)


            sz_data = {'post': post_id, 'user': user_id}
            post_react_serializer = PostReactSerializer(data=sz_data)
            
            if post_react_serializer.is_valid():
                post_react_serializer.save()
                logging.getLogger('root').debug('reaction saved')
                return Response({'message': 'reaction added'}, status=status.HTTP_201_CREATED)
            
            logger.getLogger('root').error(post_react_serializer.errors)
            logging.getLogger('root').error('serializer error')
            return Response({'message': 'some error ocurred'}, status=status.HTTP_400_BAD_REQUEST) 
        
        except Exception as e:
            logging.getLogger('root').error(str(e))
            return Response({'message': 'some error occured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
