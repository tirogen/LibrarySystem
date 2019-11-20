from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from .models import Gadget, GadgetSerializer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core import serializers

import logging

def get():
	cursor = connection.cursor()
	cursor.execute("SELECT api_gadget.Name, api_gadget.Status, api_gadget.PurchasedDate, api_room.id, api_room.RoomType_id,api_room.Name \
					FROM api_gadget \
					INNER JOIN api_room ON api_gadget.Room_id=api_room.id \
					LIMIT 20")
	response = []
	for row in cursor.fetchall():
		response.append({
			"GadgetName": row[0],
			"Status": row[1],
			"PurchasedDate": row[2],
			"RoomID": row[3],
			"RoomType": row[4],
			"RoomName": row[5]
		})
	return response

@api_view(['GET', 'POST', 'DELETE'])
def manageGadget(request):
	if request.method == 'GET':
	    res =get()
	    return Response(res)
	elif request.method == 'POST':
		Name = request.data['Name']
		Status = request.data['Status']
		Room_id = request.data['Room_id']
		PurchasedDate = request.data['PurchasedDate']
		ls = (Name,Status,PurchasedDate,Room_id)
		print(Name + Status + str(Room_id) + PurchasedDate)
		cursor = connection.cursor()
		insert_stmt = (
			"INSERT INTO api_gadget (Name, Status, PurchasedDate, Room_id)"
			"VALUES (%s, %s, %s, %s)"
		)
		cursor.execute(insert_stmt,ls)
        # Gadget.objects.raw(insert_stmt)
		res=get()
		return Response(res)
	elif request.method == 'DELETE' :
		print("this is id from DELETE request")
		print(id)
        #oom.objects.delete(id)
		return Response(status=status.HTTP_200_OK) 
