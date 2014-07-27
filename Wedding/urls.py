from django.conf.urls import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns('OneYear.views',
	url(r'^$', 'index', name='index'),
	url(r'^contact/', 'contact', name='contact'),
	url(r'^favicon\.ico$', RedirectView.as_view(url='/static/OneYear/favicon.ico')),
)
