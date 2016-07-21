from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /cam/
    url(r'^cam$', views.cam, name='cam'),
    # ex: /linked/
    url(r'^linked$', views.lnked, name='linked'),
    # ex: /new_token/
    url(r'^new_token$', views.new_token, name='new_token'),
]