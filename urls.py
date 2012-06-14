
from django.conf.urls.defaults import *


urlpatterns = patterns('dashboard.core.views',
    (r'^$','index'),
    (r'^authentication$','authentication'),
    (r'^auth-callback$','auth_callback'),
)
