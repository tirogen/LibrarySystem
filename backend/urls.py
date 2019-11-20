"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.views import index_view, MessageViewSet
from .api.punish import Penalty, CalculatePoint
from .api.reservedRoom import GetTop20, manageRoom, deleteReservedRoom
from .api.Gadget import manageGadget
from .api.book import getBook
from .api.room import roomTypes, getAvailableTimeSlot, getRoomNameByType

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
    path('api/reservedRoom/delete/<str:id>/', deleteReservedRoom),
    path('api/reservedRoom/manageRoom/', manageRoom),
    path('api/Gadget/manageGadget/', manageGadget),
    path('api/book/getBook/', getBook),

    # room
    path('api/room/types/', roomTypes),
    path('api/room/names/<str:roomType>/', getRoomNameByType),
    path('api/room/<str:roomType>/<str:date>/', getAvailableTimeSlot),
    # penalty
    path('api/punish/penalty/', Penalty),
    path('api/punish/penalty/<str:id>/', Penalty),
    path('api/punish/calculatePoint/(<str:id>/', CalculatePoint),
]
