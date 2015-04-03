from django.conf.urls import patterns, include, url
from main_site import views

urlpatterns = patterns('',
                       url(r'^contact/', include('contact_form.urls')),
                       url(r'^index/', views.index, name='index')
                       )
