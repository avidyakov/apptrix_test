from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import RegisterSerializer


class UserViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def match(self, request, pk=None):
        matched_user = self.get_object()
        self.request.user.matches.add(matched_user)

        if self.request.user.matched.filter(email=matched_user.email).exists():
            self.request.user.notify(matched_user.email)
            matched_user.notify(self.request.user.email)

        return Response(status=HTTP_201_CREATED)
