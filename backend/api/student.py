from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
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
            "studentID":row[0],
		}
        response.append(obj)
	return Response(response, status = status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def studentList(request, id=None):
    if request.method == 'GET':
        return getStudentList()