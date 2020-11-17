from rest_framework import serializers
from .models import RantPost


class RantPostSerializer(serializers.ModelSerializer):
    slug_field = serializers.SerializerMethodField('get_slug_field')

    class Meta:
        model = RantPost
        fields = ['id', 'title', 'text', 'feeling_level', 'created_on', 'author', 'slug_field']
        read_only_fields = ['author']

    def get_slug_field(self, rant_post):
        title_split = rant_post.title.split(' ')
        title_split = list(map(lambda x: x.lower(), title_split))
        return '-'.join(title_split)
