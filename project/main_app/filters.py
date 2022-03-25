import django_filters

from .models import User


class UserFilter(django_filters.FilterSet):
    distance = django_filters.NumberFilter(lookup_expr='lt')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'sex', 'distance')
