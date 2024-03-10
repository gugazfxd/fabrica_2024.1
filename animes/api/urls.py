from rest_framework.routers import DefaultRouter
from django.urls import path, include
from viewsets import AppViewSet

router= DefaultRouter()

router.register("App",AppViewSet)

urlpatterns=[
    path("api/",include(router.urls))
]