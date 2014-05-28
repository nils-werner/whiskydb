from django.conf.urls import url

from catalog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<whisky_id>[0-9]+)/$', views.detail, name='detail'),
]
