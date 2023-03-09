import django_filters
from rest_framework.viewsets import ModelViewSet

from {{path_to_app}}.api.serializers import {{MainClass}}Serializer
from {{path_to_app}}.models import {{MainClass}}


class {{MainClass}}Filter(django_filters.FilterSet):
    """Фильтр для {{MainClass}}."""

    class Meta(object):
        model = {{MainClass}}
        fields = {list_main_fields}}

class {{MainClass}}ViewSet(ModelViewSet):
    """{{docs}}"""

    queryset = {{MainClass}}.objects.all()
    serializer_class = {{MainClass}}Serializer
    filterset_class = {{MainClass}}Filter
    ordering_fields = {{list_main_fields}}
    search_fields = {{list_main_fields}}
