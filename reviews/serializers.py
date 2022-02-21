from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = (
            'id',
            'author',
            'created_on',
            'is_published',
        )

    rating = serializers.IntegerField(
        min_value=1,
        max_value=5,
    )
