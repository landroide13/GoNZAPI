
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from Api.views import TourViewSet, UserViewSet, AgentViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('tours', TourViewSet)
router.register('users', UserViewSet)
router.register('agents', AgentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
