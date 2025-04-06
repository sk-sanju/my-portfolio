from django.urls import path
from .views import HealthCheckView, APIRootView, AboutView

urlpatterns = [
    path('', APIRootView.as_view()),
    path('health/', HealthCheckView.as_view()),
    path('about/', AboutView.as_view()),
]
