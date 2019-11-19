from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from backend.api.models import Penalty, Punish


@api_view(['GET'])
def roomTypes(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM api_roomtype;")
    response = []
    for record in cursor.fetchall():
        response.append({
            "type": record[0],
            "capacity": record[1]
        })
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAvailableTimeSlot(request, type, date):
    statement = "SELECT api_room.Name, api_roomtime.Date, api_roomtime.StartTime, api_roomtime.EndTime FROM api_reserve \
                INNER JOIN api_room \
                INNER JOIN api_roomtime \
                ON api_reserve.RoomTime_id=api_roomtime.id \
                AND api_reserve.Room_id=api_room.id \
                AND api_room.RoomType_id=%s;"
    cursor = connection.cursor()
    cursor.execute(statement, [type])
    response = []
    for record in cursor.fetchall():
        response.append({
            "name": record[0],
            "date": record[1],
            "start_time": record[2],
            "end_time": record[3]
        })
    return Response(response, status=status.HTTP_200_OK)
