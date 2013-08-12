#coding:utf-8

from django.contrib import admin
from gauth.models import FlowModel, CredentialsModel

class CredentialsAdmin(admin.ModelAdmin):
    pass


class FlowAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)
admin.site.register(FlowModel, FlowAdmin)
