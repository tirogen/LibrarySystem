from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from backend.api.models import Penalty, Punish

MAX_POINT = 100


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def penalty(request, id=None):
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
        insert_id = cursor.lastrowid
        response = request.data
        response["id"] = insert_id
        return Response(response, status = status.HTTP_200_OK)
    elif(request.method == 'DELETE'):
        statement = ("DELETE FROM `api_penalty` WHERE id=%s")
        cursor = connection.cursor()
        cursor.execute(statement, [id])
        return Response({'id': id}, status = status.HTTP_200_OK)
    elif(request.method == 'PUT'):
        statement = ("UPDATE `api_penalty` SET `Name`=%s,`Point`=%s WHERE id=%s")
        cursor = connection.cursor()
        cursor.execute(statement, [request.data["Name"], request.data["Point"], request.data["id"]])
        return Response(request.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def calculatePoint(request, id):
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
            "TotalPoint": MAX_POINT - row[1]
        })
    return Response(response, status = status.HTTP_200_OK)

@api_view(['POST', 'DELETE'])
def punish(request, id=None):
    if(request.method == 'POST'):
        sid = request.data["Student_id"]
        pid = request.data["Penalty_id"]
        date = request.data["Date"]
        time = request.data["Time"]
        statement = ("INSERT INTO `api_punishtime`(`Date`, `Time`)\
                        VALUES (%s, %s);\
                        INSERT INTO `api_punish`(`Penalty_id`, `PunishTime_id`, `Student_id`)\
                        VALUES (%s, LAST_INSERT_ID(), %s)")
        cursor = connection.cursor()
        cursor.execute(statement, [date, time, pid, sid])
        insert_id = cursor.lastrowid
        response = {
            "Date": request.data["Date"],
            "Penalty": request.data["Penalty"],
            "Point": request.data["Point"],
            "Time": request.data["Time"],
            "id": insert_id
        }
        return Response(response, status = status.HTTP_200_OK)
    elif(request.method == 'DELETE'):
        statement = ("DELETE FROM `api_punish` WHERE id=%s")
        cursor = connection.cursor()
        cursor.execute(statement, [id])
        return Response({'id': id}, status = status.HTTP_200_OK)

@api_view(['GET'])
def getPunishInfo(request, FName, LName):
    statement = ("SELECT pn.id, p.Name, p.Point,pt.Date, pt.Time, s.FName, s.LName, s.Email, s.Tel, s.Username FROM `api_punish` as pn\
                    INNER JOIN `api_penalty` AS p ON pn.Penalty_id=p.id\
                    INNER JOIN `api_student` AS s ON pn.Student_id=s.Username\
                    INNER JOIN `api_punishtime` AS pt ON pn.PunishTime_id=pt.id\
                    WHERE s.FName=%s and s.LName=%s")
    cursor = connection.cursor()
    # result = cursor.execute(statement, [FName, LName])
    histories = []
    remainingPoint = MAX_POINT
    fullName = ""
    email = ""
    phoneNumber = ""
    username = ""
    for row in cursor.fetchall():
        fullName = row[5] + " " + row[6]
        email = row[7]
        phoneNumber = row[8]
        username = row[9]
        remainingPoint -= row[2]
        histories.append({
            "id": row[0],
            "Penalty": row[1],
            "Point": row[2],
            "Date": row[3],
            "Time": row[4],
        })
    response = {
        "histories": histories,
        "remainingPoint": remainingPoint,
        "fullName": fullName,
        "email": email,
        "phoneNumber": phoneNumber,
        "username": username
        }
    return Response(response, status = status.HTTP_200_OK)

