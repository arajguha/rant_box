from rest_framework import generics, mixins
from .serializers import RantPostSerializer
from .models import RantPost
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import RantPostUpdateDeletePermissions


class RantPostListCreateView(generics.ListCreateAPIView):
    serializer_class = RantPostSerializer
    queryset = RantPost.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RantPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RantPostSerializer
    queryset = RantPost.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, RantPostUpdateDeletePermissions]

