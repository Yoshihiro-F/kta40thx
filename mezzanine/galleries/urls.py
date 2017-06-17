from django.conf.urls import url
from . import views

app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.index, name='gallery'),
    url(r'^(?P<dirname>[A-Za-z0-9\-\_\.]+)/$', views.detail, name='gallery')
]
