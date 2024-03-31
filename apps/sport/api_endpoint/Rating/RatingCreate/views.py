from rest_framework.generics import CreateAPIView

from apps.sport.api_endpoint.Rating.RatingCreate.serializer import RatingCreateSerializer
from apps.sport.models import Rating


class RatingCreateAPIView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingCreateSerializer

__all__ = ['RatingCreateAPIView']