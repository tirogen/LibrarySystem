from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from rest_framework import status


def getBorrow():
    statement = ("SELECT * FROM `api_borrow`AS i\
						INNER JOIN `api_booktime` AS b ON b.id=i.BookTime_id")
    statement = ("SELECT api_borrow.Student_id, api_student.FName, api_student.Lname, \
				    api_book.Isbn_id,api_book.id,\
					api_isbn.Name,api_isbn.Category,api_isbn.Author\
					api_booktime.StartDate, api_booktime.EndDate\
					api_borrow.id\
                    FROM api_borrow\
                    INNER JOIN api_book ON api_borrow.Book_id=api_book.id\
                    INNER JOIN api_isbn ON api_book.Isbn_id=api_isbn.Isbn\
                    INNER JOIN api_booktime ON api_borrow.BookTime_id=api_booktime.id\
					INNER JOIN api_student ON api_student.Username=api_borrow.Student_id")
    cursor = connection.cursor()
    cursor.execute(statement)
    response = []
    for row in cursor.fetchall():
        obj = {
			"studentID": row[0],
			"studentName": row[1],
			"studnetSurname": row[2],
			"startDate": row[8],
			"endDate": row[9],
			"bookISBN": row[3],
			"bookID": row[4],
			"bookName": row[5],
			"bookCategory": row[6],
			"bookAuthor": row[7],
			"borrowID" : row[10]
        }
        # if row[0] in response.keys():
#     response[row[0]]["number"].append(row[4])
#     response[row[0]]["num"] = len(response[row[0]]["number"])
#     response[row[0]]["status"].append(row[5])
# else:
#     response[row[0]] = {
#         "enddate": row[1],
#         "author": row[2],
#         "name": row[3],
#         "number": [row[4]],
#         "status": [row[5]],
#         "num": 1
#     }
        response.append(obj)
    return Response(response, status=status.HTTP_200_OK)


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
        # row = cursor.fetchall()
        # iflen(row) == 0):
