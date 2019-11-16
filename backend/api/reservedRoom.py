from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import connection
from .models import Room, RoomSerializer, Librarian, LibrarianSerializer

@api_view(['GET', 'POST', 'DELETE'])
def test(request, format=None):
    print(request.method)
    if request.method == 'GET':
        room = Room.objects.raw("SELECT * FROM api_room")
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # dd = str(request.data["id"])
        # Name = request.data['Name']
        # Status = request.data['Status']
        # Librarian_id = request.data['Librarian_id']
        # print("This is from JSON POST")
        # print(dd, Name, Status, Librarian_id)
        # #Room.objects.raw("INSERT INTO api_room VALUES ("1","+Name+","+Status+","+Librarian_id+","+"'The Box')")
        # return Response(status=status.HTTP_200_OK)

        ID = str(request.data["id"])
        NAME = request.data['Name']
        STATUS = request.data['Status']
        LIB_ID = request.data['Librarian_id']
        RT_ID = request.data['RoomType_id']
        print("This is from JSON POST")
        print(ID, NAME, STATUS, LIB_ID, RT_ID)
        # Room.objects.raw("INSERT INTO api_room VALUES ("1","+Name+","+Status+","+Librarian_id+","+"'The Box')")
        cursor = connection.cursor()
        insert_stmt = (
            "INSERT INTO api_room (id, Name, Status, Librarian_id, RoomType_id)"
            "VALUES (%s, %s, %s, %s, %s)"
            )
        data = (ID,NAME,STATUS,LIB_ID,RT_ID)
        cursor.execute(insert_stmt,data)
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        print("this is id from DELETE request")
        print(id)
        #oom.objects.delete(id)
        return Response(status=status.HTTP_200_OK)