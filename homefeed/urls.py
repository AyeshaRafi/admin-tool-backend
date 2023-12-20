from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomefeedElementViewSet

router = DefaultRouter()
router.register(r'homefeed-elements', HomefeedElementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
