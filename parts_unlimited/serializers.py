from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Part


class PartSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Part
        fields = '__all__'

    def get_links(self, obj) -> list[dict[str, str]]:
        request = self.context['request']
        return [
            {
                'rel': 'self',
                'href': reverse('part-detail', kwargs={'pk': obj.pk}, request=request),
            },
            {
                'rel': 'update',
                'href': reverse('part-detail', kwargs={'pk': obj.pk}, request=request),
                'method': 'PUT'
            },
            {
                'rel': 'partial_update',
                'href': reverse('part-detail', kwargs={'pk': obj.pk}, request=request),
                'method': 'PATCH'
            },
            {
                'rel': 'delete',
                'href': reverse('part-detail', kwargs={'pk': obj.pk}, request=request),
                'method': 'DELETE'
            },
            {
                'rel': 'list',
                'href': reverse('part-list', request=request),
                'method': 'GET'
            }
        ]


class CommonWordsSerializer(serializers.Serializer):
    word = serializers.CharField()
    count = serializers.IntegerField()