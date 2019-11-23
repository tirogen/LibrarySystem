from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from rest_framework import status

@api_view(['GET', 'POST', 'DELETE'])
def book(request, id=None):
	if request.method == 'GET':
		statement = ("SELECT * FROM `api_isbn`AS i\
						INNER JOIN `api_book` AS b ON b.Isbn_id=i.Isbn") 
		cursor = connection.cursor()
		cursor.execute(statement)
		response = {}
		for row in cursor.fetchall():
			if row[0] in response.keys():
				response[row[0]]["number"].append(row[4])
			else:
				response[row[0]] = {
					"category": row[1],
					"author": row[2],
					"name": row[3],
					"number": [row[4]]
				}
		return Response(response, status = status.HTTP_200_OK)

	elif request.method == 'DELETE':
		cursor = connection.cursor()
		statement = ("SELECT Isbn_id FROM `api_book` WHERE id=%s")
		cursor.execute(statement, [id])
		isbn = cursor.fetchall()[0][0]
		statement = ("DELETE FROM `api_book` WHERE id=%s")
		cursor.execute(statement, [id])
		statement = ("SELECT * FROM `api_book` WHERE Isbn_id=%s")
		cursor.execute(statement, [isbn])
		row = cursor.fetchall()
		if(len(row) == 0):
			statement = ("DELETE FROM `api_isbn` WHERE Isbn=%s")
			cursor.execute(statement, [isbn])
		return Response({'id': id, 'isbn': isbn}, status = status.HTTP_200_OK)
		
	elif request.method == 'POST':
		if request.data["name"] == "":
			statement = ("INSERT INTO `api_book`(`Status`,`Isbn_id`)\
							VALUES ('Available', %s);")
			cursor = connection.cursor()
			cursor.execute(statement, [request.data["isbn"]])
			insert_id = cursor.lastrowid
			return Response({'id': insert_id, 'isbn': request.data["isbn"]}, status = status.HTTP_200_OK)
		else:
			statement = ("INSERT INTO `api_isbn`(`Isbn`, `Category`, `Author`, `Name`) VALUES (%s, %s, %s, %s);")
			cursor = connection.cursor()
			cursor.execute(statement, [request.data["isbn"], request.data["category"], request.data["author"], request.data["name"]])
			statement = ("INSERT INTO `api_book`(`Status`,`Isbn_id`) VALUES ('Available', %s);")
			cursor.execute(statement, [request.data["isbn"]])
			insert_id = cursor.lastrowid
			return Response({'id': insert_id, 'isbn': request.data["isbn"]}, status = status.HTTP_200_OK)
