from user.views import login_view, register, index, upload, createfolder, logout_view, download, delete, rename, \
    validate, forgot, o, frename, fdelete, profile

o
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login_view),
    url(r'^logout/$', logout_view),
    url(r'^register/$', register),
    url(r'^index/$', index),
    url(r'^upload/$', upload),
    url(r'^createfolder/$', createfolder),
    url(r'^download/$', download),
    url(r'^delete/$', delete),
    url(r'^rename/$', rename),
    url(r'^open/$', o),
    url(r'^forgot/$', forgot),
    url(r'^frename/$', frename),
    url(r'^validate/$', validate),
    url(r'^fdelete/$', fdelete),
    url(r'^profile/$', profile),
]
