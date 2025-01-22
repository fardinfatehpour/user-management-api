from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ArticleViewSet, NewsEventViewSet, UpcomingEventViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'news-events', NewsEventViewSet)
router.register(r'upcoming-events', UpcomingEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
