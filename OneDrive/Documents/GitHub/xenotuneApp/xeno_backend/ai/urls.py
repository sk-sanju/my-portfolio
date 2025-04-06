from django.urls import path
from .views import MoodDetectionView

urlpatterns = [
    path('mood/', MoodDetectionView.as_view()),
]
