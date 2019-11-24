from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
from rest_framework import status

from django.db import connection


@api_view(['GET'])
def getBorrowingBook(request, id):
    statement = ("SELECT api_book.id, api_isbn.Name, api_booktime.StartDate, api_booktime.EndDate, api_booktime.RenewTimes\
                    FROM api_borrow\
                    INNER JOIN api_book ON api_borrow.Book_id=api_book.id\
                    INNER JOIN api_isbn ON api_book.Isbn_id=api_isbn.Isbn\
                    INNER JOIN api_booktime ON api_borrow.BookTime_id=api_booktime.id\
                    where api_borrow.Student_id = %s;")
    cursor = connection.cursor()
    cursor.execute(statement, [id])
    response = []
    for row in cursor.fetchall():
        response.append({
            "ID": row[0],
            "BookName": row[1],
            "BorrowDate": row[2],
            "ReturnDate": row[3],
            "RenewTime": row[4]
        })
    return Response(response, status = status.HTTP_200_OK)