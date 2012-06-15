
from django.conf.urls.defaults import *


urlpatterns = patterns('example.gauth.views',
    (r'^$','index'),
    (r'^authentication$','authentication'),
    (r'^auth-callback$','auth_callback'),
)
