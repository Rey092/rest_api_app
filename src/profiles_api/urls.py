from django.urls import path, include

from rest_framework.routers import DefaultRouter

from src.profiles_api.views import HelloApiView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-view-set', HelloViewSet, basename='hello-view-set')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello-view', HelloApiView.as_view()),
    path('', include(router.urls)),
]
