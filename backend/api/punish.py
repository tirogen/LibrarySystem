from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from backend.api.models import Penalty, Punish


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Penalty(request, id=None):
    if(request.method == 'GET' and id==None):
        statement = ("SELECT * FROM api_penalty;")
        cursor = connection.cursor()
        cursor.execute(statement)
        response = []
        for col in cursor.fetchall():
            response.append({
                "id": col[0],
                "Name": col[1],
                "Point": col[2]
            })
        return Response(response, status = status.HTTP_200_OK)
    elif(request.method == 'POST'):
        statement = ("INSERT INTO `api_penalty`(`Name`, `Point`) VALUES (%s, %s)")
        cursor = connection.cursor()
        cursor.execute(statement, [request.data["Name"], request.data["Point"]])
        return Response(request.data, status = status.HTTP_200_OK)
    elif(request.method == 'DELETE'):
        statement = ("DELETE FROM `api_penalty` WHERE id=%s")
        cursor = connection.cursor()
        return Response(id, status = status.HTTP_200_OK)

@api_view(['GET'])
def CalculatePoint(request, id):
    statement = ("SELECT api_punish.Student_id ,SUM(api_penalty.Point) TotalPoint\
                    FROM api_punish\
                    INNER JOIN api_penalty ON api_punish.Penalty_id = api_penalty.id\
                    WHERE api_punish.Student_id = %s;")
    cursor = connection.cursor()
    cursor.execute(statement, [id])
    response = []
    for row in cursor.fetchall():
        response.append({
            "Student_id": row[0],
            "TotalPoint": 100 - row[1]
        })
    return Response(response, status = status.HTTP_200_OK)

# @api_view(['POST', 'DELETE'])
# def Punish(request, id=None):
#     if(request.method == 'POST'):
#         Sid = int(request.data["Student_id")
#         Pid = int(request.data["Penalty_id"])

#         statement = ("INSERT INTO `api_punish`(`FName`, `LName`, `Penalty_id`) VALUES (%s, %s, %i)")
#         cursor = connection.cursor()
#         cursor.execute(statement, [])
#         return Response(request.data, status = status.HTTP_200_OK)


@api_view(['GET'])
def GetPunishInfo(request, FName, LName):
    statement = ("SELECT pn.id, s.FName, s.LName, p.Name, pt.Date, pt.Time FROM `api_punish` as pn\
                    LEFT JOIN `api_penalty` AS p ON pn.Penalty_id=p.id\
                    LEFT JOIN `api_student` AS s ON pn.Student_id=s.Username\
                    LEFT JOIN `api_punishtime` AS pt ON pn.PunishTime_id=pt.id\
                    WHERE s.FName=%s and s.LName=%s")
    cursor = connection.cursor()
    cursor.execute(statement, [FName, LName])
    response = []
    for row in cursor.fetchall():
        response.append({
            "ID": row[0],
            "Firstname": row[1],
            "Lastname": row[2],
            "Penalty": row[3],
            "Date": row[4],
            "Time": row[5]
        })
    return Response(response, status = status.HTTP_200_OK)

