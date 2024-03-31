from rest_framework.generics import DestroyAPIView

from apps.sport.api_endpoint.Rating.RatingDestroy.serializer import RatingDestroySerializer
from apps.sport.models import Rating


class RatingDestroyAPIView(DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingDestroySerializer

__all__ = ['RatingDestroyAPIView']