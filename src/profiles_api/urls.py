from django.urls import path

from src.profiles_api.views import HelloApiView

urlpatterns = [
    path('', HelloApiView.as_view()),
]
