"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.views import index_view, MessageViewSet
from .api.punish import penalty, calculatePoint, getPunishInfo, punish
from .api.reservedRoom import getReservedRooms, manageRoom, deleteReservedRoom, checkInReservedRoom, checkOutReservedRoom
from .api.Gadget import manageGadget
from .api.book import book
from .api.room import roomTypes, getAvailableTimeSlot, getRoomNameByType, bookForRoom, getActiveReservation, cancelReservation
from .api.borrowBook import manageBorrowBook
from .api.borrow import getBorrowingBook

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    path('api/reservedRoom/getReservedRooms/', getReservedRooms),
    path('api/reservedRoom/delete/<str:id>/', deleteReservedRoom),
    path('api/reservedRoom/checkIn/<str:id>/', checkInReservedRoom),
    path('api/reservedRoom/checkOut/<str:id>/', checkInReservedRoom),
    path('api/reservedRoom/manageRoom/', manageRoom),
    path('api/Gadget/manageGadget/', manageGadget),
    path('api/Gadget/manageGadget/<str:id>/', manageGadget),
    #manage book
    path('api/book/book/', book),
    path('api/book/book/<str:id>/', book),

    #penalty
    path('api/punish/penalty/', penalty),
    path('api/punish/calculatePoint/<str:id>/', calculatePoint),
    path('api/punish/penalty/<str:id>/', penalty),
    path('api/punish/getPunishInfo/<str:FName>/<str:LName>/', getPunishInfo),
    path('api/punish/punish/<str:id>/', punish),
    path('api/punish/punish/', punish),
    # room
    path('api/room/types/', roomTypes),
    path('api/room/names/<str:roomType>/', getRoomNameByType),
    path('api/room/bookForRoom/', bookForRoom),
    path('api/room/<str:roomType>/<str:date>/', getAvailableTimeSlot),
    #student
    path('api/student/reservation/active/<str:studentId>/<str:date>/', getActiveReservation),
    path('api/student/reservation/<str:reservationId>/', cancelReservation),
    path('api/student/borrowing/<str:id>/', getBorrowingBook),

    #borrow
    path('api/borrow/borrow/',manageBorrowBook)
    # path('api/borrow/book/<str:id>/', getBorrow)
]
