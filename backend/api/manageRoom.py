from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from backend.api.models import Penalty, Punish

MAX_POINT = 100


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def roomType(request, id=None):
    if request.method == "GET":
        statement = ("SELECT Type, Capacity FROM `api_roomtype`")
        cursor = connection.cursor()
        cursor.execute(statement)
        response = []
        for row in cursor.fetchall():
            response.append({
            "Type": row[0],
            "Capacity": row[1]
        })
        return Response(response)

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
        return Response(response, status = status.HTTP_200_OK)

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
    
# def room(request, id=None):
#      if request.method == "GET":
#         statement = ("SELECT Type, Capacity FROM `api_roomtype`")
#         cursor = connection.cursor()
#         cursor.execute(statement)
#         response = []
#         for row in cursor.fetchall():
#             response.append({
#             "Type": row[0],
#             "Capacity": row[1]
#         })
#         return Response(response)

