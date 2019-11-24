from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from rest_framework import status

def getBorrow():
	statement = ("SELECT * FROM `api_borrow`AS i\
						INNER JOIN `api_booktime` AS b ON b.id=i.BookTime_id") 
	cursor = connection.cursor()
	cursor.execute(statement)
	response = {}
	for row in cursor.fetchall():
		if row[0] in response.keys():
			response[row[0]]["number"].append(row[4])
			response[row[0]]["num"] = len(response[row[0]]["number"])
			response[row[0]]["status"].append(row[5])
		else:
			response[row[0]] = {
				"enddate": row[1],
				"author": row[2],
				"name": row[3],
				"number": [row[4]],
				"status": [row[5]],
				"num" : 1
			}
	return Response(response, status = status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def manageBorrowBook(request, id=None):
	if request.method == 'GET':
		return getBorrow()

	elif request.method == 'DELETE':
		cursor = connection.cursor()
		statement = ("SELECT BookTime_id FROM `api_borrow` WHERE id=%s")
		cursor.execute(statement, [id])
		bookTimeID = cursor.fetchall()[0][0]
		statement = ("DELETE FROM `api_borrow` WHERE id=%s")
		cursor.execute(statement, [id])
		statement = ("SELECT * FROM `api_booktime` WHERE id=%s")
		cursor.execute(statement, [bookTimeID])
		row = cursor.fetchall()
		# iflen(row) == 0):
