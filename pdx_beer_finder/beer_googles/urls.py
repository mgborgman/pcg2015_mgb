from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',

                       url(r'^index$', views.index, name='index'),
                       url(r'^$', views.welcome, name='welcome'),
                       url(r'^register$', views.register, name='register'),
                       url(r'^signin$', views.signin, name='signin'),
                       url(r'^success$', views.success, name='success'),
                       url(r'^bars/(?P<bar_slug>[\w\-]+)/$', views.bars, name='bars'),
                       url(r'^beers/(?P<beer_slug>[\w\-]+)/$', views.beers, name='beers'),
                       url(r'^logout$', views.logout_view, name='logout'),

                       )