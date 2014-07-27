from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectADK.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Wedding.urls', namespace='Wedding')),
    url(r'^admin/', include(admin.site.urls)),
) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
