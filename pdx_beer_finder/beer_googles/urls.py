from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',

                       url(r'^index$', views.index, name='index'),
                       url(r'^$', views.welcome, name='welcome'),
                       url(r'^register$', views.register, name='register'),
                       url(r'^signin$', views.signin, name='signin'),
                       url(r'^success$', views.success, name='success'),

                       )