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
def CalculatePoint(request, id):
    statement = ("SELECT api_punish.Student_id ,SUM(api_penalty.Point) TotalPoint\
                                FROM api_punish\
                                INNER JOIN api_penalty\
                                ON api_punish.Penalty_id = api_penalty.id\
                                WHERE api_punish.Student_id = %s;")
    cursor = connection.cursor()
    cursor.execute(statement, [id])
    response = []
    for col in cursor.fetchall():
        response.append({
            "Student_id": col[0],
            "TotalPoint": 100 - col[1]
        })
    return Response(response, status=status.HTTP_200_OK)
