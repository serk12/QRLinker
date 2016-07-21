from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /cam/
    url(r'^cam$', views.cam, name='cam'),
]