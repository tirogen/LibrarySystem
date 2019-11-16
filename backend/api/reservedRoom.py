from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Room, RoomSerializer, Librarian, LibrarianSerializer


class getTop20(viewsets.ModelViewSet):
    queryset = Librarian.objects.raw("\
        SELECT * FROM api_room\
        INNER JOIN api_librarian ON api_room.Librarian_id=api_librarian.Username\
        WHERE id=3;")
    serializer_class = LibrarianSerializer
    serializer_class = LibrarianSerializer
