from django.http import HttpResponse
from django.db import connection


def history_view(request):
    '''
    Check if
    '''

    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM south_migrationhistory''')
        r = cursor.fetchone()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(r)


def delete_migration(request):
    try:
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM south_migrationhistory
                       WHERE id=1''')
        r = cursor.fetchone()

    except Exception as e:
        return HttpResponse(e)
    return HttpResponse(r)
