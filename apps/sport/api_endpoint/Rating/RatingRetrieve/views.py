from rest_framework.generics import RetrieveAPIView

from apps.sport.api_endpoint.Rating.RatingRetrieve.serializer import (
    RatingRetrieveSerializer,
)
from apps.sport.models import Rating


class RatingRetrieveAPIView(RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingRetrieveSerializer


__all__ = ["RatingRetrieveAPIView"]
