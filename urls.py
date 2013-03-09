# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', views.news_page),
    url(r'^contacts$', views.contacts_page),
    url(r'^licenses$', views.licenses_page),
    url(r'^evidences$', views.evidences_page),
    url(r'^contacts/(?P<contact_id>\w+)$' , views.contacts_page),
    url(r'^page/(?P<page_name>\w+)$' , views.get_page),
    url(r'^insert_test_data$', views.insert_test_data),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),   
)
