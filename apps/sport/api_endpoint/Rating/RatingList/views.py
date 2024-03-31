from rest_framework.generics import ListAPIView

from apps.sport.api_endpoint.Rating.RatingList.serializer import RatingListSerializer
from apps.sport.models import Rating


class RatingListAPIView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingListSerializer


__all__ = ["RatingListAPIView"]
