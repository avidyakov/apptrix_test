from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import RegisterSerializer


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @action(detail=True, methods=['post'])
    def match(self, request, pk=None):
        if not self.request.user:
            raise PermissionDenied

        matched_user = self.get_object()
        self.request.user.matches.add(matched_user)
        return Response(status=HTTP_201_CREATED)
