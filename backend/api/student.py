from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection, Error
from rest_framework import status


def getStudentList():
    statement = ("SELECT api_borrow.Student_id\
                    FROM api_borrow\
			        INNER JOIN api_student ON api_student.Username=api_borrow.Student_id")
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for row in cursor.fetchall():
        obj = {
            "studentID": row[0],
        }
        response.append(obj)
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'DELETE'])
def studentList(request, id=None):
    if request.method == 'GET':
        return getStudentList()


@api_view(['GET'])
def getStudentNameById(request, studentId):
    statement = "SELECT FName, LName FROM api_student WHERE Username='{}'".format(studentId)
    cursor = connection.cursor()
    response = []
    cursor.execute(statement)
    try:
        records = cursor.fetchall()
        if len(records) == 0:
            return Response([], status.HTTP_204_NO_CONTENT)
        else:
            for record in records:
                response.append({
                    'FirstName': record[0],
                    'LastName' : record[1]
                })
            return Response(response, status=status.HTTP_200_OK)
    except Error:
        return Response([], status=status.HTTP_500_INTERNAL_SERVER_ERROR)
