"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from .api.views import index_view, MessageViewSet
# from .api.reservedRoom import GetTop20
from .api.reservedRoom import test

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
# router.register(r'reservedRoom/getTop20', GetTop20)

urlpatterns = [

    path('test/', test),

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]
