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
def getRoomNameByType(request, roomType):
    cursor = connection.cursor()
    cursor.execute("SELECT api_room.Name FROM api_room WHERE api_room.RoomType_id='{}';".format(roomType))
    response = []
    for record in cursor.fetchall():
        response.append({
            "name": record[0]
        })
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAvailableTimeSlot(request, roomType, date):
    statement = "SELECT api_room.Name, api_roomtime.Date, api_roomtime.StartTime, api_roomtime.EndTime FROM api_reserve \
                INNER JOIN api_room \
                INNER JOIN api_roomtime \
                ON api_reserve.RoomTime_id=api_roomtime.id \
                AND api_reserve.Room_id=api_room.id \
                AND api_room.RoomType_id='{}' \
                WHERE api_roomtime.Date='{}';".format(roomType, date)
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for record in cursor.fetchall():
        response.append({
            "name": record[0],
            "date": record[1],
            "start_time": record[2],
            "end_time": record[3]
        })
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def bookForRoom(request):
    statement1 = "INSERT INTO api_roomtime(StartTime, EndTime, Date) VALUES('{}', '{}', '{}');".format('startTime', 'endTime', 'date')
    statement2 = "INSERT INTO api_reserve(TimeIn, TimeOut, Room_id, RoomTime_id, Student_id) VALUES(NULL, NULL, {}, @@IDENTITY, '{}');".format('roomId', 'studentId')
    statement3 = "INSERT INTO api_reservefriend(Friend_id, Reserve_id) VALUES('{}', @@IDENTITY);".format('friendId')
    #statement 3 need loop if multiple friendId
    statement = statement1 + statement2 + statement3
    cursor = connection.cursor()
    # cursor.execute(statement)
    response = [request.POST]
    # for record in cursor.fetchall():
    #     response.append({
    #         "name": record[0],
    #         "date": record[1],
    #         "start_time": record[2],
    #         "end_time": record[3]
    #     })
    return Response(response, status=status.HTTP_200_OK)