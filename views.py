#coding:utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from gauth.models import CredentialsModel
from gauth.models import FlowModel
from oauth2client.django_orm import Storage
from oauth2client.client import OAuth2WebServerFlow
from gauth_settings import GA_ARGS

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def authentication(request):
    user = request.user
    redirect_uri = "http://%s/gauth/auth-callback" % request.get_host()
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid == True:
        flow = OAuth2WebServerFlow(client_id=GA_ARGS['client_id'],
            client_secret=GA_ARGS['client_secret'],
            scope=GA_ARGS['scope'],
            user_agent=GA_ARGS['user_agent'],
            access_type="offline")

        authorize_url = flow.step1_get_authorize_url(redirect_uri)
        f = FlowModel(id=user, flow=flow)
        f.save()
        return HttpResponseRedirect(authorize_url)
    else:
        return HttpResponse("OK")

def auth_callback(request):
    user = request.user
    try:
        f = FlowModel.objects.get(id=user)
        credential = f.flow.step2_exchange(request.REQUEST)
        storage = Storage(CredentialsModel, 'id', user, 'credential')
        storage.put(credential)
        f.delete()
        return HttpResponseRedirect("/")
    except FlowModel.DoesNotExist:
        return HttpResponse("ERRO")
