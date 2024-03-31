from django.urls import path

from apps.sport.api_endpoint.Chempionship import (
    ChempionshipListAPIView,
    ChempionshipCreateAPIView,
    ChempionshipUpdateAPIView,
    ChempionshipDestroyAPIView,
    ChempionshipRetrieveAPIView,
)
from apps.sport.api_endpoint.Match import (
    MatchListAPIView,
    MatchCreateAPIView,
    MatchUpdateAPIView,
    MatchDestroyAPIVIew,
)
from apps.sport.api_endpoint.Match.MatchRetrieve.views import MatchRetrieveAPIView
from apps.sport.api_endpoint.Rating import (
    RatingListAPIView,
    RatingCreateAPIView,
    RatingUpdateAPIView,
    RatingDestroyAPIView,
    RatingRetrieveAPIView,
)
from apps.sport.api_endpoint.Sport import (
    SportListAPIView,
    SportCreateAPIView,
    SportUpdateAPIView,
    SportDestroyAPIView,
    SportRetrieveAPIView,
)
from apps.sport.api_endpoint.Team import (
    TeamListAPIView,
    TeamCreateAPIView,
    TeamUpdateAPIView,
    TeamDestroyAPIView,
    TeamRetrieveAPIView,
)

urlpatterns = [
    # sport
    path("sport/", SportListAPIView.as_view()),
    path("sport/create/", SportCreateAPIView.as_view()),
    path("sport/<pk>/update/", SportUpdateAPIView.as_view()),
    path("sport/<pk>/destroy/", SportDestroyAPIView.as_view()),
    path("sport/<pk>/retrieve/", SportRetrieveAPIView.as_view()),
    # chempionship
    path("chempionship/", ChempionshipListAPIView.as_view()),
    path("chempionship/create/", ChempionshipCreateAPIView.as_view()),
    path("chempionship/<pk>/update/", ChempionshipUpdateAPIView.as_view()),
    path("chempionship/<pk>/destroy/", ChempionshipDestroyAPIView.as_view()),
    path("chempionship/<pk>/retrieve/", ChempionshipRetrieveAPIView.as_view()),
    # team
    path("team/", TeamListAPIView.as_view()),
    path("team/create/", TeamCreateAPIView.as_view()),
    path("team/<pk>/update/", TeamUpdateAPIView.as_view()),
    path("team/<pk>/destroy", TeamDestroyAPIView.as_view()),
    path("team/<pk>/retrieve/", TeamRetrieveAPIView.as_view()),
    # match
    path("match/", MatchListAPIView.as_view()),
    path("match/create/", MatchCreateAPIView.as_view()),
    path("match/<pk>/update/", MatchUpdateAPIView.as_view()),
    path("match/<pk>/destroy/", MatchDestroyAPIVIew.as_view()),
    path("match/<pk>/retrieve/", MatchRetrieveAPIView.as_view()),
    # rating
    path("rating/", RatingListAPIView.as_view()),
    path("rating/create/", RatingCreateAPIView.as_view()),
    path("rating/<pk>/update/", RatingUpdateAPIView.as_view()),
    path("rating/<pk>/destroy/", RatingDestroyAPIView.as_view()),
    path("rating/<pk>/retrieve/", RatingRetrieveAPIView.as_view()),
]
