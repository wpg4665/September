from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('Wedding.urls', namespace='Wedding')),
    url(r'^admin/', include(admin.site.urls)),
)
