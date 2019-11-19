from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
def get():
	cursor = connection.cursor()
	cursor.execute("SELECT api_book.id, api_book.Isbn_id, api_book.Status \
					FROM api_book \
					LIMIT 20")
	response = []
	for row in cursor.fetchall():
		response.append({
			"id": row[0],
			"ISBN": row[1],
			"Status": row[2],
		})
	return response

@api_view(['GET', 'POST', 'DELETE'])
def getBook(request):
	if request.method == 'GET':
	    res =get()
	    return Response(res)
	elif request.method == 'POST':
        # Name = request.data['Name']
        # Status = request.data['Status']
        # RoomType_id = request.data['RoomType_id']
		print("ANKASDASDDA")
		# insert_stmt = (
		# 	"INSERT INTO api_gadget (Name, Status, PurchasedDate, RoomType_id)"
		# 	"VALUES (%s, %s, %s, %s, %s)"
		# )
        # Gadget.objects.raw(insert_stmt)
		res=get()
		return Response(data=res)
	elif request.method == 'DELETE':
		print("this is id from DELETE request")
		print(id)
        #oom.objects.delete(id)
		return Response(status=status.HTTP_200_OK) 
