from django.conf.urls import patterns, include, url
from . import views, feed


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^blog$', views.BlogIndex.as_view(), name='blog_index'),
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
    url(r'^blog/entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)