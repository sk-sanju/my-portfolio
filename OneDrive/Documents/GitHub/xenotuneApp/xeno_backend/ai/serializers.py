from rest_framework import serializers

class MoodDetectionSerializer(serializers.Serializer):
    audio = serializers.FileField()

class MoodResponseSerializer(serializers.Serializer):
    mood = serializers.CharField()
    confidence = serializers.FloatField()
    recommendations = serializers.ListField(
        child=serializers.CharField()
    )
