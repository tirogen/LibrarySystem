from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Reserve, ReserveSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

@api_view(['GET', 'POST', 'DELETE'])
def GetTop20(request, format=None):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute("SELECT api_room.Name, api_reserve.TimeIn, api_reserve.TimeOut, api_student.FName, api_student.LName \
                        FROM api_reserve \
                        INNER JOIN api_room ON api_reserve.Room_id=api_room.id \
                        INNER JOIN api_student ON api_reserve.Student_id=api_student.Username")
        response = []
        for row in cursor.fetchall():
            response.append({
                "Room": row[0],
                "Time In": row[1],
                "Time Out": row[2],
                "Name": row[3]+" "+row[4],
            })
        return Response(response)
