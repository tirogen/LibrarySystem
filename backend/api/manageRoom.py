from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from backend.api.models import Penalty, Punish

MAX_POINT = 100


def getRoomType():
    statement = ("SELECT Type, Capacity FROM `api_roomtype`")
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for row in cursor.fetchall():
        response.append({
        "Type": row[0],
        "Capacity": row[1]
    })
    return Response(response, status = status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def roomType(request, id=None):
    if request.method == "GET":
        return getRoomType()

    elif request.method == "POST":
        Type = request.data["Type"]
        Capacity = request.data["Capacity"]
        statement = ("INSERT INTO `api_roomtype`(`Type`, `Capacity`) VALUES (%s, %s);")
        cursor = connection.cursor()
        cursor.execute(statement, [Type, Capacity])
        insert_id = cursor.lastrowid
        response = {
            "Type": request.data["Type"],
            "Capacity": request.data["Capacity"],
        }
        return getRoomType()

    elif request.method == "DELETE":
        statement = ("DELETE FROM `api_roomtype` WHERE Type=%s")
        cursor = connection.cursor()
        cursor.execute(statement, [id])
        return Response({'Type': id}, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        statement = ("UPDATE `api_roomtype` SET `Type`=%s,`Capacity`=%s WHERE `Type`=%s")
        Type = request.data["Type"]
        OldType = request.data["OldType"]
        Capacity = request.data["Capacity"]
        cursor = connection.cursor()
        cursor.execute(statement, [Type, Capacity, OldType])
        return Response(request.data, status = status.HTTP_200_OK)

def getRoom():
    statement = ("SELECT r.id, r.Name, l.FName, l.LName, t.Type FROM `api_room` AS r\
                        INNER JOIN `api_librarian` AS l ON r.Librarian_id=l.Username\
                        INNER JOIN `api_roomtype` AS t ON t.Type=r.RoomType_id")
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for row in cursor.fetchall():
        response.append({
            "id": row[0],
            "Name": row[1],
            "LibrarianName": row[2] + " " + row[3],
            "Type": row[4]
        })
    return Response(response, status = status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])   
def room(request, id=None):
    if request.method == "GET":
        return getRoom()

    elif request.method == 'DELETE':
        statement = ("DELETE FROM `api_room` WHERE id=%s")
        cursor = connection.cursor()
        cursor.execute(statement, [id])
        return Response({"id": id}, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        statement = ("INSERT INTO `api_room`(`Name`, `Status`, `Librarian_id`, `RoomType_id`)\
                        VALUES (%s,%s,%s,%s)")
        cursor = connection.cursor()
        cursor.execute(statement, [request.data["Name"], "Available",request.data["LibrarianUsername"], request.data["Type"]])
        return getRoom()
    
    elif request.method == 'PUT':
        statement = ("UPDATE `api_room`\
                        SET `Name`=%s,`Librarian_id`=%s,`RoomType_id`=%s\
                        WHERE id=%s")
        cursor = connection.cursor()
        cursor.execute(statement, [request.data["Name"], request.data["LibrarianUsername"], request.data["Type"], request.data["id"]])
        statement = ("SELECT FName, LName FROM `api_librarian` WHERE Username=%s")
        cursor.execute(statement, [request.data["LibrarianUsername"]])
        row = cursor.fetchall()[0]
        response = {
            "Name": request.data["Name"],
            "id": request.data["id"],
            "Type": request.data["Type"],
            "LibrarianName": row[0] + " " + row[1]
        }
        return Response(response, status = status.HTTP_200_OK)


@api_view(['GET'])
def getAllLibrarians(request):
    statement = ("SELECT Username, FName, LName FROM `api_librarian`")
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for row in cursor.fetchall():
        response.append({
            "Username": row[0],
            "LibrarianName": row[1] + " " + row[2],
        })
    return Response(response, status = status.HTTP_200_OK)