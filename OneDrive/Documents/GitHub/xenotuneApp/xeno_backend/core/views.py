from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class HealthCheckView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class APIRootView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({
            "message": "Welcome to the Xenotune API",
            "version": "v1.0",
            "endpoints": {
                "auth": "/api/users/",
                "ai": "/api/ai/",
                "core": "/api/core/",
            }
        })


class AboutView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({
            "company": "Xenotrix Technologies",
            "product": "Xenotune",
            "mission": "Bringing AI-powered audio experiences to everyone.",
            "location": "Kerala, India",
            "contact": "xenotrixtech@gmail.com"
        })
