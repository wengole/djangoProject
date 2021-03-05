from rest_framework import serializers

from api.models import Consumer


class ConsumerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Consumer
        fields = "__all__"
