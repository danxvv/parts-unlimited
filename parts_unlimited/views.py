from collections import Counter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import extend_schema
from django.core.cache import cache
from .filters import PartFilter
from .serializers import PartSerializer, CommonWordsSerializer
from .models import Part
from .utils import most_common_words


from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(
        description="Retrieve a list of parts, optionally filtered by is_active",
        responses={200: PartSerializer(many=True)},
    ),
    retrieve=extend_schema(
        description="Retrieve a single part by ID.",
        responses={200: PartSerializer},
    ),
    create=extend_schema(
        description="Create a new part.",
        request=PartSerializer,
        responses={201: PartSerializer},
    ),
    update=extend_schema(
        description="Update an existing part.",
        request=PartSerializer,
        responses={200: PartSerializer},
    ),
    partial_update=extend_schema(
        description="Partially update an existing part.",
        request=PartSerializer,
        responses={200: PartSerializer},
    ),
    destroy=extend_schema(
        description="Delete an existing part.",
        responses={204: None},
    )
)
class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all().order_by('id')
    serializer_class = PartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PartFilter



@extend_schema(
    description="Retrieve the 5 most common words in the descriptions of all parts.",
    responses={200: CommonWordsSerializer}
)
class CommonWordsView(GenericAPIView):
    serializer_class = CommonWordsSerializer
    schema = AutoSchema()

    def get(self, request, *args, **kwargs):
        cache_key = 'common_words'
        data = cache.get(cache_key)
        if data is None:
            descriptions = Part.objects.values_list('description', flat=True)
            data = most_common_words(descriptions)
            cache.set(cache_key, data, timeout=60)
        return Response(data)