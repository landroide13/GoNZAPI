
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from Api.views import TourViewSet, UserViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('tours', TourViewSet)
router.register('users', UserViewSet)
router.register('agents', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
