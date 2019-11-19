"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.views import index_view, MessageViewSet
from .api.reservedRoom import GetTop20, getRoom
from .api.punish import GetAllPenalty, CalculatePoint
from .api.Gadget import getGadget
from .api.book import getBook

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    path('api/reservedRoom/getTop20/', GetTop20),
    path('api/reservedRoom/getRoom/', getRoom),
    path('api/Gadget/getGadget/', getGadget),
    path('api/book/getBook/',getBook),


    #penalty
    path('api/punish/getAllPenalty/', GetAllPenalty),
    path('api/punish/calculatePoint/<str:id>/', CalculatePoint)
]
