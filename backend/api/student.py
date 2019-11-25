from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection, Error
from rest_framework import status


def getStudentList():
    statement = ("SELECT api_student.Username\
                    FROM api_student")
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for row in cursor.fetchall():
        # obj = {
        #     "studentID": row[0],
        # }
        response.append(row[0])
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
def studentList(request):
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
                    'Firstname': record[0],
                    'Lastname' : record[1]
                })
            return Response(response, status=status.HTTP_200_OK)
    except Error:
        return Response([], status=status.HTTP_500_INTERNAL_SERVER_ERROR)
