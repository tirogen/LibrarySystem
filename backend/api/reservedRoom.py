from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from rest_framework import status
import datetime

@api_view(['GET'])
def GetTop20(request):
    cursor = connection.cursor()
    cursor.execute("SELECT api_room.Name, api_roomtime.id, \
                            api_reserve.TimeIn, api_reserve.TimeOut, \
                            api_student.FName, api_student.LName, \
                            api_roomtime.StartTime, api_roomtime.EndTime, api_roomtime.Date, \
                            api_reserve.id \
                    FROM api_reserve \
                    INNER JOIN api_room ON api_reserve.Room_id=api_room.id \
                    INNER JOIN api_student ON api_reserve.Student_id=api_student.Username \
                    INNER JOIN api_roomtime ON api_reserve.RoomTime_id=api_roomtime.id \
                    WHERE api_roomtime.Date = CURDATE() \
                    ORDER BY api_roomtime.StartTime \
                    LIMIT 20")
    response = []
    for row in cursor.fetchall():
        response.append({
            "Room": row[0],
            "TimeIn": row[2],
            "TimeOut": row[3],
            "Name": row[4]+" "+row[5],
            "StartTime": row[6],
            "EndTime": row[7],
            "Date": row[8],
            "RoomTime_id": row[1],
            "id": row[9]
        })
    return Response(response)

@api_view(['DELETE'])
def deleteReservedRoom(request, id = None):
    if(request.method == 'DELETE' and id != None):
        cursor = connection.cursor()
        res = cursor.execute("DELETE FROM api_roomtime WHERE id = " + id)
        return Response(res)

@api_view(['PATCH'])
def checkInReservedRoom(request, id = None):
    if(request.method == 'PATCH' and id != None):
        cursor = connection.cursor()
        cursor.execute("UPDATE api_reserve SET TimeIn = NOW() WHERE id = " + id)
        cursor.execute("SELECT TimeIn FROM api_reserve WHERE id = " + id)
        return Response(cursor.fetchone())

@api_view(['PATCH'])
def checkOutReservedRoom(request, id = None):
    if(request.method == 'PATCH' and id != None):
        cursor = connection.cursor()
        cursor.execute("UPDATE api_reserve SET TimeOut = NOW() WHERE id = " + id)
        cursor.execute("SELECT TimeOut FROM api_reserve WHERE id = " + id)
        return Response(cursor.fetchone())

@api_view(['GET','POST'])
def manageRoom(request) :
    cursor = connection.cursor()
    cursor.execute("SELECT api_room.id, api_room.Name, api_room.RoomType_id FROM api_room")
    obj = dict()
    # obj = {
    #         roomType : {
    #           roomName: id,
    #         },
    # }
    for row in cursor.fetchall():
        room_id = row[0];
        roomName = row[1];
        roomType = row[2];
        if obj == dict() :
            obj = {
                roomType : {
                    roomName : room_id
                }
            }
        elif roomType not in obj.keys() :
            obj[roomType] = {
                roomName : room_id
            }
        else :
            if roomName not in obj[roomType].keys():
                obj[roomType][roomName] = room_id
    return Response(obj)
