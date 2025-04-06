from django.urls import path
from .views import RegisterView, CustomLoginView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', CustomLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
]