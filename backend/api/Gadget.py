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
	cursor.execute("SELECT api_gadget.Name, api_gadget.Status, api_gadget.PurchasedDate, api_room.id, api_room.RoomType_id,api_room.Name, api_gadget.id \
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
			"RoomName": row[5],
			"GadgetID": row[6]
		})
	return response


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def manageGadget(request, id=None):
	if request.method == 'GET':
	    res = get()
	    return Response(res)
	elif request.method == 'POST':
		Name = request.data['Name']
		Status = request.data['Status']
		Room_id = request.data['Room_id']
		PurchasedDate = request.data['PurchasedDate']
		ls = (Name, Status, PurchasedDate, Room_id)
		print(Name + Status + str(Room_id) + PurchasedDate)
		cursor = connection.cursor()
		insert_stmt = (
			"INSERT INTO api_gadget (Name, Status, PurchasedDate, Room_id)"
			"VALUES (%s, %s, %s, %s)")
		cursor.execute(insert_stmt,ls)
		res=get()
		return Response(res)
	elif request.method == 'PUT' : 
		print("DETECTED")
		statement = ("UPDATE `api_gadget` SET `Name`=%s,`Status`=%s, `PurchasedDate`=%s, `Room_id`=%s WHERE id=%s")
		cursor = connection.cursor()
		cursor.execute(statement, [request.data["Name"], request.data["Status"], request.data["PurchasedDate"], request.data["Room_id"], request.data["id"]])
        # not detect status how to know it was successful
		print("asdasd")
		cursor2 = connection.cursor()
		cursor2.execute("SELECT api_gadget.Name, api_gadget.Status, api_gadget.PurchasedDate, api_room.id, api_room.RoomType_id,api_room.Name, api_gadget.id \
				FROM api_gadget \
				INNER JOIN api_room ON api_gadget.Room_id=api_room.id \
				WHERE api_gadget.id=%d",list(request.data["id"])
				)
			
		print("asdasd")
		row = cursor2.fetchone()
		response = {
			"GadgetName": row[0],
			"Status": row[1],
			"PurchasedDate": row[2],
			"RoomID": row[3],
			"RoomType": row[4],
			"RoomName": row[5],
			"GadgetID": row[6]
		}
		return Response(response, status = status.HTTP_200_OK)
	elif request.method == 'DELETE' :
		# print("this is id from DELETE request")
		# print(id)
		statement = ("DELETE FROM `api_gadget` WHERE id=%s")
		cursor = connection.cursor()
		cursor.execute(statement, [id])
		return Response({'id': id}, status = status.HTTP_200_OK)
