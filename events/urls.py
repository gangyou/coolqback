from django.conf.urls import patterns, include, url
from events import views

urlpatterns = patterns('events',
    url(r'^$', views.index),
)