from django.contrib.gis.db.models.functions import GeometryDistance
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from .filters import UserFilter
from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_permissions(self):
        if self.action == 'create':
            return AllowAny(),

        return IsAuthenticated(),

    def get_queryset(self):
        return User.objects.annotate(distance=GeometryDistance('location', self.request.user.location))

    @action(detail=True, methods=['post'])
    def match(self, request, pk=None):
        matched_user = self.get_object()
        self.request.user.matches.add(matched_user)

        if self.request.user.matched.filter(email=matched_user.email).exists():
            self.request.user.notify(matched_user.email)
            matched_user.notify(self.request.user.email)

        return Response(status=HTTP_201_CREATED)
