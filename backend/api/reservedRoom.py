from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

@api_view(['GET', 'POST', 'DELETE'])
def GetTop20(request):
    cursor = connection.cursor()
    cursor.execute("SELECT api_room.Name, api_reserve.TimeIn, api_reserve.TimeOut, api_student.FName, api_student.LName \
                    FROM api_reserve \
                    INNER JOIN api_room ON api_reserve.Room_id=api_room.id \
                    INNER JOIN api_student ON api_reserve.Student_id=api_student.Username \
                    LIMIT 20")
    response = []
    for row in cursor.fetchall():
        response.append({
            "Room": row[0],
            "Time In": row[1],
            "Time Out": row[2],
            "Name": row[3]+" "+row[4],
        })
    return Response(response)

@api_view(['GET'])
def getRoom(request) :
    cursor = connection.cursor()
    cursor.execute("SELECT api_room.id, api_room.Name, api_room.RoomType_id FROM api_room")
    response = []
    for row in cursor.fetchall():
        obj = {
            "id": row[0],
            "roomName": row[1],
            "roomType": row[2],
        }
        if obj not in response :
            response.append(obj)
    return Response(response)
