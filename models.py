#coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField

class FlowModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    flow = FlowField()


class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()


class CredentialsAdmin(admin.ModelAdmin):
    pass


class FlowAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)
admin.site.register(FlowModel, FlowAdmin)
