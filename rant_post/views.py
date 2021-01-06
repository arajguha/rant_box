import logging

from rest_framework import generics
from .serializers import RantPostSerializer, PostReactSerializer
from .models import RantPost, PostReact
from rest_framework.permissions import IsAuthenticated
from .permissions import RantPostUpdateDeletePermissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


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
    """ React to a post. Add and remove reaction """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.user.id
            post_id = request.data['post_id']

            post = RantPost.objects.filter(pk=post_id)
            if not post.exists():
                logging.getLogger('root').error('post does not exists. invalid post id')
                return Response({'message': 'post does not exists. invalid post id'}, status=status.HTTP_400_BAD_REQUEST)

            reactions = PostReact.objects.filter(post=post_id)
            for reaction in reactions:
                if reaction.user.id == user_id:
                    # user already reacted. Hence remove reaction record
                    reaction.delete()
                    return Response({
                        'message': 'reaction removed',
                        'reaction_status': False
                    }, status=status.HTTP_200_OK)

            # user not reacted. Add reaction record
            sz_data = {'post': post_id, 'user': user_id}
            post_react_serializer = PostReactSerializer(data=sz_data)
            
            if post_react_serializer.is_valid():
                post_react_serializer.save()

                logging.getLogger('root').debug('reaction saved')
                return Response({
                    'message': 'reaction added', 
                    'reaction_status': True
                }, status=status.HTTP_201_CREATED)
            
            logger.getLogger('root').error(post_react_serializer.errors)
            logging.getLogger('root').error('serializer error')
            return Response({'message': 'some error ocurred'}, status=status.HTTP_400_BAD_REQUEST) 
        
        except Exception as e:
            logging.getLogger('root').error(str(e))
            return Response({'message': 'some error occured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reaction_info_view(request, post_id):
    """ returns info related to reactions for a particular post """

    post_reactions = PostReact.objects.filter(post=post_id)
    
    if not post_reactions.exists():
        return Response({
            'post_id': post_id,
            'users_list': 0,
            'self_reacted': False
        }, status=status.HTTP_200_OK)

    users_list = []
    self_reacted = False
    for reaction in post_reactions:
        if reaction.user == request.user:
            self_reacted = True
        users_list.append(reaction.user.username)

    return Response({
        'post_id': post_id,
        'users_count': len(users_list),
        'self_reacted': self_reacted
    }, status=status.HTTP_200_OK)

    #return Response('testing')
