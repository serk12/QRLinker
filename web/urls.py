from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /cam/
    url(r'^cam$', views.cam, name='cam'),
    # ex: /linked/
    url(r'^linked$', views.linked, name='linked'),
    # ex: /new_token/
    url(r'^new_token$', views.new_token, name='new_token'),
    # ex: /registry_token/
    url(r'^registry_token', views.registry_token, name='registry_token'),
    # ex: /is_registred/
    url(r'^is_registred', views.is_registred, name='is_registred'),
    # ex: /uploadFile/
    url(r'^uploadFile', views.uploadFile, name='uploadFile'),
    # ex: /downloadFile/
    url(r'^downloadFile', views.downloadFile, name='downloadFile'),

]
