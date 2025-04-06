from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import MoodDetectionSerializer, MoodResponseSerializer
from .utils import detect_mood, recommend_soundscape

import os
from django.core.files.storage import default_storage

class MoodDetectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = MoodDetectionSerializer(data=request.data)
        if serializer.is_valid():
            audio = serializer.validated_data['audio']
            file_path = default_storage.save(f"temp/{audio.name}", audio)
            full_path = os.path.join(default_storage.location, file_path)

            # Run mood detection
            mood_result = detect_mood(full_path)
            recommendations = recommend_soundscape(mood_result["mood"])

            # Clean up temp file
            default_storage.delete(file_path)

            response = {
                "mood": mood_result["mood"],
                "confidence": mood_result["confidence"],
                "recommendations": recommendations
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
