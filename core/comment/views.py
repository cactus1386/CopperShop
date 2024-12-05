from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product_id')
        if product_id:
            queryset = queryset.filter(product_id=product_id)
        return queryset
