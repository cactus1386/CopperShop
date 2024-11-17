from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import SliderSerializer
from .models import Slider


class SliderViews(ListCreateAPIView):
    permission_classes = []
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()
