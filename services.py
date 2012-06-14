#coding: utf-8

from oauth2client.django_orm import Storage
from apiclient.discovery import build
import httplib2
from gauth.models import CredentialsModel
from django.contrib.auth.models import User
from settings import GA_ARGS, GA_FILTERS
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar


def get_service():
    user = User.objects.get(username='<username>')
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()
    http = httplib2.Http()
    http = credential.authorize(http)
    service = build("analytics", "v3", http=http)

    return service

def get_ga():
    service = get_service()
    return service.data().ga()


def sum_session_by(start_date, end_date, filters, max_results=10000):
    ga = get_ga()
    response = ga.get(ids=GA_ARGS['ids'],
            start_date=str(start_date),
            end_date=str(end_date),
            metrics=GA_ARGS['metrics'],
            max_results=max_results,
            filters=filters).execute()

    rows = response.get('rows')
    operations = []
    result = 0
    if rows:
        for row in rows:
            volume = int(row[0])
            if volume:
                result += volume

    return result
