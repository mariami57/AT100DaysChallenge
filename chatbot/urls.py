import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from chatbot.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]