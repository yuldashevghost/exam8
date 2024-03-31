from rest_framework.generics import UpdateAPIView

from apps.sport.api_endpoint.Rating.RatingUpdate.serializer import RatingUpdateSerializer
from apps.sport.models import Rating


class RatingUpdateAPIView(UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingUpdateSerializer

__all__ = ['RatingUpdateAPIView']