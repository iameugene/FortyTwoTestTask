from django.http import HttpResponse
from django.db import connection


def history_view(request):

    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM south_migrationhistory''')
        r = cursor.fetchone()
        cursor.execute('''SELECT * FROM  hello_personalinfo''')
        r1 = cursor.fetchone()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse('%s \n %s' % r, r1)
