from django.conf.urls import url
from . import views

app_name = 'planning'
urlpatterns = [
    url(r'^$', views.index, name='planning'),
    url(r'^(?P<year>[0-9]{4})/$', views.lastyear, name='planning'),
]