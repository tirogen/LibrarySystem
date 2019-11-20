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
	cursor.execute("SELECT api_gadget.Name, api_gadget.Status, api_gadget.PurchasedDate, api_room.Name \
					FROM api_gadget \
					INNER JOIN api_room ON api_gadget.Room_id=api_room.id \
					LIMIT 20")
	response = []
	for row in cursor.fetchall():
		response.append({
			"GadgetName": row[0],
			"Status": row[1],
			"PurchasedDate": row[2],
			"RoomName": row[3],
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
		RoomType_id = request.data['RoomType_id']
		PurchasedDate = request.data['PurchasedDate']
		print(Name + Status + RoomType_id + PurchasedDate)
	
		# cursor = connection.cursor()
		# insert_stmt = (
		# 	"INSERT INTO api_gadget (Name, Status, PurchasedDate, RoomType_id)"
		# 	"VALUES (%s, %s, %s, %s)"
		# )
		# cursor.execute(insert_stmt,request)
        # Gadget.objects.raw(insert_stmt)
		res=get()
		return Response(res)
	elif request.method == 'DELETE' :
		print("this is id from DELETE request")
		print(id)
        #oom.objects.delete(id)
		return Response(status=status.HTTP_200_OK) 
