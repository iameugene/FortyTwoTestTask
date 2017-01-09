from django.http import HttpResponse
from django.db import connection


def history_view(request):

    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM south_migrationhistory''')
    r = cursor.fetchone()
    return HttpResponse(r)
